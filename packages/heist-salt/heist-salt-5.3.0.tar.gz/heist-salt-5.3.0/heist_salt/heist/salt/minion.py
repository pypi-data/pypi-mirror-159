import asyncio
import copy
import os
import pathlib
import secrets
import sys
import warnings
from typing import Any
from typing import Dict

import asyncssh
from packaging.version import Version


async def run(
    hub,
    remotes: Dict[str, Dict[str, str]],
    artifact_version=None,
    **kwargs,
):
    if not hub.OPT.heist.onedir:
        warnings.warn(
            "Support for singlebin will be removed in version 6.0.0. Please use onedir packages by passing in --onedir",
            DeprecationWarning,
        )
    coros = []
    for id_, remote in remotes.items():
        coro = hub.heist.salt.minion.single(
            remote,
            artifact_version=artifact_version,
        )
        coros.append(coro)
    async_kwargs = {"return_exceptions": False}
    if sys.version_info == (3, 6):
        async_kwargs["loop"] = hub.pop.Loop
    await asyncio.gather(*coros, **async_kwargs)


async def single(
    hub,
    remote: Dict[str, Any],
    artifact_version=None,
):
    """
    Execute a single async connection
    """
    # create tunnel
    target_name = secrets.token_hex()
    hub.heist.ROSTERS[target_name] = hub.pop.data.imap(copy.copy(remote))
    tunnel_plugin = remote.get("tunnel", "asyncssh")
    minion_id = remote.get("id")
    bootstrap = remote.get("bootstrap", False)
    hub.log.debug("Creating SSH Tunnel")
    if not await hub.heist.salt.minion.manage_tunnel(
        target_name, tunnel_plugin, remote=remote, bootstrap=bootstrap
    ):
        return False

    hub.log.debug("Detecting target os and arch")
    target_os, target_os_arch = await hub.tool.system.os_arch(
        target_name, tunnel_plugin
    )
    hub.log.debug(f"Found target_os: {target_os}")

    if not hub.OPT.heist.offline_mode:
        pkg_type = "singlebin/"
        if hub.OPT.heist.onedir:
            pkg_type = "onedir/"
        salt_repo_url = hub.OPT.heist.salt_repo_url + pkg_type
        repo_data = await hub.artifact.salt.repo_data(salt_repo_url)
        if isinstance(repo_data, dict) and not artifact_version:
            latest = repo_data.get("latest")
            if latest:
                artifact_version = repo_data["latest"][next(iter(latest))]["version"]
            else:
                artifact_version = max(repo_data.keys(), key=lambda x: Version(x))

        if artifact_version:
            hub.log.debug(f"Getting artifact for {target_os}")
            if not await hub.artifact.init.get(
                "salt",
                target_os=target_os,
                version=artifact_version,
                repo_data=repo_data,
                salt_repo_url=salt_repo_url,
                artifacts_dir=pathlib.Path(hub.tool.artifacts.get_artifact_dir()),
            ):
                return False

    # Get salt minion user
    user = remote.get("username")
    if not user:
        user = hub.heist.init.default(target_os, "user")
    hub.log.debug(f"Using remote user: {user}")

    run_dir_root = hub.heist.init.default(target_os, "run_dir_root")
    if target_os == "windows":
        run_dir = hub.tool.path.path_convert(
            target_os,
            run_dir_root,
            ([f"heist_{user}", f"{secrets.token_hex()[:4]}"]),
        )
    else:
        run_dir = hub.tool.path.path_convert(
            target_os,
            run_dir_root,
            (["tmp", f"heist_{user}", f"{secrets.token_hex()[:4]}"]),
        )
    hub.log.debug(f"Validating path: {run_dir}")
    if not hub.tool.path.clean_path(run_dir_root, run_dir):
        hub.log.error(f"The run_dir {run_dir} is not a valid path")
        return False
    hub.heist.CONS[target_name] = {"run_dir": run_dir}

    # Deploy
    binary = hub.artifact.salt.latest("salt", version=artifact_version)
    hub.log.debug(f"Deploying artifact: {binary}")
    binary_path = await hub.artifact.salt.deploy(
        target_name,
        tunnel_plugin,
        run_dir,
        binary,
        user=user,
        target_os=target_os,
        minion_id=minion_id,
        bootstrap=bootstrap,
    )
    if not binary_path:
        hub.log.error(f"Could not deploy the artifact to the target {remote['id']}")
        return False

    hub.log.debug("Getting target grains")
    grains = await hub.salt.call.init.get_grains(
        target_name, tunnel_plugin, run_dir, target_os
    )
    hub.log.debug("Getting target grains complete")

    # Don't log out {remote} as it contains SSH password
    hub.log.debug("Getting service plugin")
    service_plugin = hub.service.init.get_service_plugin(remote, grains)
    hub.log.debug(f"Found service plugin: {service_plugin}")

    hub.heist.CONS[target_name].update(
        {
            "tunnel_plugin": tunnel_plugin,
            "manager": "salt.minion",
            "service_plugin": service_plugin,
            "target_os": target_os,
            "target_os_arch": target_os_arch,
        }
    )

    hub.log.debug("Getting minion opts")
    minion_opts = hub.tool.config.get_minion_opts(
        run_dir=run_dir,
        target_name=target_name,
        target_os=target_os,
        minion_id=minion_id,
        bootstrap=bootstrap,
    )
    hub.log.debug("Getting minion opts complete")

    hub.log.debug(f"Connecting to {target_name}")
    if not await hub.heist.salt.minion.manage_tunnel(
        target_name,
        tunnel_plugin,
        create=False,
        tunnel=True,
        minion_opts=minion_opts,
        bootstrap=bootstrap,
    ):
        hub.log.error(f"Failed to connect to {target_name}")
        return False

    # generate keys
    if hub.OPT.heist.generate_keys and not bootstrap:
        hub.log.debug(f"Generating keys for {target_name}")
        await hub.salt.key.init.generate_keys(
            target_name,
            tunnel_plugin,
            run_dir,
            user=user,
            minion_id=minion_id,
            target_os=target_os,
        )

    # Start minion
    hub.log.debug("Starting the minion")
    hub.log.debug(f"Target '{remote.id}' is using service plugin: {service_plugin}")
    await hub.service.salt.minion.start(
        target_name,
        tunnel_plugin,
        service_plugin,
        run_dir=run_dir,
        target_os=target_os,
    )

    hub.log.debug(
        f"Starting infinite loop on {remote.id}. "
        f"Checkin time: {hub.OPT.heist.checkin_time}"
    )

    while True:
        if not hub.tunnel[tunnel_plugin].connected(target_name):
            # we lost connection, lets check again to see if we can connect
            hub.log.error(f"Lost connection to {minion_id}, trying to reconnect")
            if await hub.heist.salt.minion.manage_tunnel(
                target_name,
                tunnel_plugin,
                remote=remote,
                create=True,
                tunnel=True,
                reconnect=True,
                minion_opts=minion_opts,
            ):
                hub.log.info(f"Reconnected to {minion_id} successfully.")
            else:
                hub.log.error(f"Could not connect to {minion_id}")

        await asyncio.sleep(hub.OPT.heist.checkin_time)
        if hub.OPT.heist.dynamic_upgrade:
            latest = hub.artifact.salt.latest("salt")
            if latest != binary:
                binary = latest
                await hub.artifact.salt.update(
                    target_name, tunnel_plugin, latest, binary_path, run_dir
                )


async def clean(hub, target_name, tunnel_plugin, service_plugin, vals):
    """
    Clean up the connections
    """
    # clean up service files
    await hub.service.init.clean(
        target_name,
        tunnel_plugin,
        hub.tool.service.get_service_name(service_plugin),
        service_plugin,
    )
    # clean up run directory and artifact
    await hub.artifact.init.clean(target_name, tunnel_plugin)

    minion_id = hub.heist.CONS[target_name].get("minion_id")
    if minion_id:
        if not hub.salt.key.init.delete_minion(minion_id):
            hub.log.error(f"Could not delete the key for minion: {minion_id}")


async def manage_tunnel(
    hub,
    target_name,
    tunnel_plugin,
    remote=None,
    create=True,
    tunnel=False,
    reconnect=False,
    minion_opts=None,
    bootstrap=False,
):
    # Create tunnel back to master
    if create:
        hub.log.debug(f'Connecting to host: {remote["host"]}')
        created = await hub.tunnel[tunnel_plugin].create(
            target_name, remote, reconnect=reconnect
        )
        if not created:
            hub.log.error(f'Connection to host {remote["host"]} failed')
            return False

        hub.log.info(f'Connection to host {remote["host"]} success')

    if tunnel and not bootstrap:
        import salt.config
        import salt.syspaths

        master_opts = salt.config.client_config(
            pathlib.Path(salt.syspaths.CONFIG_DIR) / "master"
        )
        hub.log.debug(f"Establishing SSH tunnel with {minion_opts['id']}")
        try:
            await hub.tunnel[tunnel_plugin].tunnel(
                target_name,
                minion_opts["publish_port"],
                master_opts.get("publish_port", 4505),
            )
            await hub.tunnel[tunnel_plugin].tunnel(
                target_name,
                minion_opts["master_port"],
                master_opts.get("master_port", 4506),
            )
            hub.log.info(f"Established SSH tunnel with {minion_opts['id']}")
        except asyncssh.misc.ChannelListenError as err:
            hub.log.error(f"Could not establish SSH tunnel with {minion_opts['id']}")
            return False
    return True
