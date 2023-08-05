"""
    artifact module to manage the download of salt artifacts
"""
import hashlib
import os
import pathlib
import re
import shutil
import sys
import tempfile
import urllib
import warnings
from pathlib import Path

import aiohttp
from packaging.version import Version


async def repo_data(hub, salt_repo_url):
    """
    Query repo.json file to gather the repo data
    """
    salt_repo_url = urllib.parse.urljoin(salt_repo_url, "repo.json")
    async with aiohttp.ClientSession() as session:
        data = await hub.artifact.init.fetch(session, salt_repo_url)
        if not data:
            hub.log.critical(
                f"Query to {salt_repo_url} failed, falling back to"
                f"pre-downloaded artifacts"
            )
            return False
        return data


async def get(
    hub,
    target_os: str = "linux",
    version: str = "",
    repo_data: dict = None,
    salt_repo_url: str = "",
    session=None,
    tmpdirname=None,
) -> str:
    """
    Download artifact if does not already exist.
    """
    try:
        artifact = [x for x in repo_data[version].keys() if target_os in x][0]
    except IndexError:
        hub.log.error(f"The version {version} was not found for {target_os}")
        return False
    verify_artifact = re.compile(f"salt-{version}.*{target_os}.*")
    if not verify_artifact.search(artifact):
        hub.log.error(f"The artifact {artifact} is not a valid Salt artifact")
        return False
    artifact_url = urllib.parse.urljoin(salt_repo_url, version + "/" + artifact)
    if not isinstance(tmpdirname, Path):
        hub.log.error(f"The tmp dir {tmpdirname} is not a pathlib.Path instance")
        return False

    if not isinstance(session, aiohttp.ClientSession):
        hub.log.error(f"The session is not a aiohttp.ClientSession instance")
        return False

    # Ensure that artifact directory exists
    artifacts_dir = hub.tool.artifacts.get_artifact_dir()
    location = Path(artifacts_dir, artifact)
    if not hub.tool.path.clean_path(artifacts_dir, artifact):
        hub.log.error(f"The {artifact} is not in the correct directory")
        return False

    # check to see if artifact already exists
    if hub.artifact.salt.latest("salt", version=version):
        hub.log.info(f"The Salt artifact {version} already exists")
        return location

    # download artifact
    hub.log.info(f"Downloading the artifact {artifact} to {artifacts_dir}")
    tmp_artifact_location = Path(tmpdirname) / artifact
    await hub.artifact.init.fetch(
        session, artifact_url, download=True, location=tmp_artifact_location
    )
    if not hub.artifact.init.verify(
        tmp_artifact_location,
        hash_value=repo_data[version][artifact]["SHA3_512"],
        hash_type="sha3_512",
    ):
        hub.log.critical(f"Could not verify the hash of {location}")
        return False
    hub.log.info(f"Verified the hash of the {artifact} artifact")
    return tmp_artifact_location


def latest(hub, name: str, version: str = "") -> str:
    """
    Given the artifacts directory return the latest desired artifact

    :param str version: Return the artifact for a specific version.
    """
    names = []
    paths = {}

    artifacts_dir = hub.tool.artifacts.get_artifact_dir()
    if not os.path.isdir(artifacts_dir):
        return ""
    for fn in os.listdir(artifacts_dir):
        if fn.startswith(name):
            ver = fn.split("-")
            if len(ver) > 4:
                ver = ver[1] + "-" + ver[2]
            else:
                ver = ver[1]
            names.append(ver)
            paths[ver] = fn
    names = sorted(names, key=Version)
    if version:
        if version in names:
            return os.path.join(artifacts_dir, paths[version])
        else:
            return ""
    elif not paths:
        return ""
    else:
        return os.path.join(artifacts_dir, paths[names[-1]])


async def deploy(
    hub,
    target_name: str,
    tunnel_plugin: str,
    run_dir: str,
    binary: str,
    user=None,
    target_os="linux",
    minion_id=None,
    bootstrap=False,
):
    """
    Deploy the salt minion to the remote system
    """
    root_dir = run_dir / "root_dir"
    binary_path = run_dir / "salt"
    conf_dir = root_dir / "conf"
    conf_tgt = conf_dir / "minion"
    is_windows = target_os == "windows"

    if not hub.tool.path.clean_path(
        hub.heist.init.default(target_os, "run_dir_root"), run_dir
    ):
        hub.log.error(f"The path {run_dir} is not a valid path")
        return False

    if not hub.tool.path.clean_path(hub.tool.artifacts.get_artifact_dir(), binary):
        hub.log.error(f"The path {binary} is not a valid path")
        return False

    config = hub.tool.config.mk_config(
        config=hub.tool.config.get_minion_opts(
            run_dir,
            target_name,
            target_os=target_os,
            minion_id=minion_id,
            bootstrap=bootstrap,
        )
    )
    if not config:
        hub.log.error(
            "Could not create the minion configuration to copy to the target."
        )
        return False

    # create dirs and config
    hub.log.debug(f"Create and secure config dir and parent directories: {conf_dir}")
    if is_windows:
        # Owner (OW), System (SY), and Administrators (BA) have Full Control
        sddl = "D:PAI(A;OICI;FA;;;OW)(A;OICI;FA;;;SY)(A;OICI;FA;;;BA)"
        owner = r'[System.Security.Principal.NTAccount]"BUILTIN\Administrators"'
        cmd = "; ".join(
            [
                f'New-Item -Path "{root_dir}", "{conf_dir}" -Type Directory',
                f'$acl = Get-Acl "{root_dir}"',
                f'$acl.SetSecurityDescriptorSddlForm("{sddl}")',
                f"$acl.SetOwner({owner})",
                f'Set-Acl -Path "{root_dir}" -AclObject $acl',
            ]
        )
    else:
        perms = 0o710 if hub.tunnel.asyncssh.CONS[target_name].get("sudo") else 0o700
        # mkdir will not add the correct permissions to the parent directories
        # unless each directory is specified
        cmd = f"mkdir -m{perms:o} -p {root_dir.parent.parent} {root_dir.parent} {root_dir} {conf_dir}"
    ret = await hub.tunnel[tunnel_plugin].cmd(target_name, cmd, target_os=target_os)

    if user and not is_windows:
        ret = await hub.tunnel[tunnel_plugin].cmd(
            target_name,
            f"chown -R {user}:{user} {root_dir.parent.parent}",
        )

    if ret.returncode != 0 or ret.stderr:
        hub.log.error(f"Could not make {conf_dir} or {root_dir} on remote host")
        hub.log.error(ret.stderr)
        return False
    try:
        await hub.tunnel[tunnel_plugin].send(target_name, config, conf_tgt)
    except Exception as e:
        hub.log.error(str(e))
        hub.log.error(f"Failed to send {config} to {target_name} at {conf_tgt}")
    finally:
        if not sys.platform == "win32":
            os.remove(config)
    # Create tmp dir and unzip/untar the artifact and copy over
    hub.log.info(f"Preparing to ship salt to {root_dir}")

    # Copy the artifact to the run_dir
    with tempfile.TemporaryDirectory() as tmpdirname:
        hub.artifact.init.extract(tmpdir=tmpdirname, binary=binary)
        recurse = False
        copy_item = "salt"
        if hub.OPT.heist.onedir:
            recurse = True
        elif target_os == "windows":
            # On Windows we need to add the extension if it is singlebin
            copy_item = "salt.exe"
            binary_path = f"{binary_path}.exe"
        copy_items = [str(Path(tmpdirname) / copy_item)]
        # On Windows we also need to copy the ssm.exe binary
        # If it is onedir, it gets copied down as part of the zip
        if target_os == "windows" and not hub.OPT.heist.onedir:
            copy_items.append(str(Path(tmpdirname) / "ssm.exe"))
        await hub.tunnel[tunnel_plugin].send(
            target_name,
            copy_items,
            run_dir,
            preserve=True,
            recurse=recurse,
        )
    if target_os == "windows":
        # Everyone (WD) has read and execute
        # System (SY) and Administrators (BA) have Full Control
        sddl = "D:PAI(A;OICI;0x1200a9;;;WD)(A;OICI;FA;;;SY)(A;OICI;FA;;;BA)"
        owner = r'[System.Security.Principal.NTAccount]"BUILTIN\Administrators"'
        cmd = "; ".join(
            [
                f'$acl = Get-Acl "{binary_path}"',
                f'$acl.SetSecurityDescriptorSddlForm("{sddl}")',
                f"$acl.SetOwner({owner})",
                f'Set-Acl -Path "{binary_path}" -AclObject $acl',
            ]
        )
    else:
        cmd = f"chmod 744 {binary_path}"
    await hub.tunnel[tunnel_plugin].cmd(target_name, cmd, target_os=target_os)
    return binary_path
