#! /usr/bin/python3

from typing import Tuple, List, Union, Dict, Optional, Any
import types
import os
import sys
from pathlib import Path
import shlex
from subprocess import Popen, PIPE
import argparse
import logging

import yaml


T_Path = Union[str, Path]
T_Dir_Dict = Dict[str, Dict[str, Any]]


def check_host_given(args: types.SimpleNamespace, host):
    """Check if the given host is online.

    :code:`args.host` overrides :code:`host`. See :func:`check_host` for details
    of how it's checked

    Args:
        args: Namespace of commandline arguments
        host: Any other host specified via config

    """
    logger = logging.getLogger("backup-rsync")
    host = args.host or host
    if not host:
        logger.error("No host found from config or command line arguments")
        sys.exit(1)
    if not check_host(host) and not args.print_only:
        logger.error(f"Host {host} not reachable")
        sys.exit(1)


def check_host(host: str, port: int = 22) -> bool:
    """Check if a given host:port combination is online

    Uses :code:`nc` process to perform the check.

    Args:
        host: name or addr of host
        port: port to check

    Example:
        >>> check_host("localhost", 22)
        True

        >>> check_host("localhost", 23)
        False

    """
    if "@" in host:
        host = host.split("@")[1]
    logger = logging.getLogger("backup-rsync")
    p = Popen(shlex.split(f"nc -z -v {host} {port}"), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate(timeout=1)
    output = err.decode("utf-8").lower()
    if "sent" in output and "received" in output:
        return True
    elif "no route" in output:
        return False
    elif "connection refused" in output:
        return False
    else:
        logger.error(f"Unknown output {output}")
        return False


def check_root_path(args: types.SimpleNamespace, root_path: T_Path):
    """Check if the root path in args or given root_path exists

    Args:
        args: Namespace of commandline arguments
        root_path: Root path in config

    """
    logger = logging.getLogger("backup-rsync")
    root_path = args.root_path or root_path
    if not root_path:
        logger.error("Root path could not be determined. Check config or give at command line")
        sys.exit(1)
    if not Path(root_path).exists():
        logger.error("Root path doesn't exist")
        sys.exit(1)


def check_dirs_all(args: types.SimpleNamespace, dirs: T_Dir_Dict) -> T_Dir_Dict:
    """Check directories read from configuration file for backup

    Args:
        args: Command line arguments
        dirs: Dictionary of directories and flags


    """
    logger = logging.getLogger("backup-rsync")
    if not dirs:
        logger.error("Cannot backup \"all\" if no supported dirs in config file")
        sys.exit(1)
    if args.exclude_projects:
        dirs = {k: v for k, v in dirs.items() if k != "projects"}
    else:
        dirs = dirs
    return dirs


def check_dirs_given(args: types.SimpleNamespace, dirs: T_Dir_Dict) -> T_Dir_Dict:
    """Check given directories for backup

    Args:
        args: Command line arguments
        dirs: Dictionary of directories and flags


    If directories are given, check for flags in config. In case :code:`dirs` are not in
    config check appropriate switches and set backup options.

    """
    logger = logging.getLogger("backup-rsync")
    # dirs = cond([(not args.unsupported and dirs,
    #               {d: dirs[d] for d in args.dirs.split(",")
    #                if d in dirs}),
    #              (not args.force)])
    if args.diff:
        dirs = {d: {"delete": args.delete} for d in args.dirs.split(",")}
    elif not args.unsupported and dirs:
        dirs = {d: dirs[d] for d in args.dirs.split(",")
                if d in dirs}
    else:
        if not args.force:
            dirs = {d: {"delete": False} for d in args.dirs.split(",")}
            args.dry_run = True
            logger.info("Only Dry Running with delete=False on unsupported. " +
                        "Set \"--force\" and \"--delete\" respectively if this is not what you want.")
        else:
            dirs = {d: {"delete": args.delete} for d in args.dirs.split(",")}
    return dirs


def check_dirs(args: types.SimpleNamespace, dirs: T_Dir_Dict) -> T_Dir_Dict:
    """Check and update the delete flag for directories.

    Args:
        args: Command line arguments
        dirs: Dictionary of directories and flags

    The dirs given may be one of \"all\" or as a comma separated list.

    """
    logger = logging.getLogger("backup-rsync")
    if not args.dirs:
        logger.error("Directories to backup must be specified")
        sys.exit(1)
    elif args.dirs == "all":
        dirs = check_dirs_all(args, dirs)
    else:
        dirs = check_dirs_given(args, dirs)
    return dirs


def check_delete_flag(args: types.SimpleNamespace, dirs: T_Dir_Dict):
    """Check and update the delete flag for directories.

    Args:
        args: Command line arguments
        dirs: Dictionary of directories and flags


    """
    logger = logging.getLogger("backup-rsync")
    if args.no_delete:
        for k, v in dirs.items():
            v.update({"delete": False})
    if args.delete and dirs:
        if not args.force and not args.diff:
            logger.error("Need \"--force\" to override \"--delete\" for configured directories")
            sys.exit(1)
        else:
            for k, v in dirs.items():
                v.update({"delete": True})


def run_cmd(cmd: List[str]) -> Tuple[str, str]:
    """Run a command `cmd`, capture stdout and stderr and return them as strings

    Args:
        cmd: The shell command

    """
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return out.decode("utf-8"), err.decode("utf-8")


def rsync_subr(user_host: str, dir_a: T_Path, dir_b: Optional[T_Path] = None,
               from_remote: bool = False, delete: bool = False,
               dry_run: bool = False, print_only: bool = False):
    """Subroutine that actually calls `rsync`

    Args:
        user_host: user@host string
        dir_a: Source directory
        dir_b: target directory
        from_remote: If True then copy from the host instead of copying to the host
        delete: `--delete` flag of `rsync`
        dry_run: `--dry-run` flag of `rsync`
        print_only: Only print the `rsync` command. Don't actually do anything.
                    Not even dry run.


    """
    logger = logging.getLogger("backup-rsync")
    if not dir_b:
        dir_b = dir_a
    dir_a = str(Path(dir_a).absolute())
    dir_b = str(Path(dir_b).absolute())
    if not dir_a.endswith("/"):
        dir_a += "/"
    if not dir_b.endswith("/"):
        dir_b += "/"
        if from_remote:
            msg = f"Backing up {user_host}:{dir_b} to {dir_a}."
        else:
            msg = f"Backing up {dir_a} to {user_host}:{dir_b}."
    if delete:
        msg += " Deleting also."
    else:
        msg += " Not deleting"
    logger.info(msg)
    if dry_run:
        logger.info("DRY RUN")
    delete = "--delete" if delete else ""  # type: ignore
    dry_run = "n" if dry_run else ""       # type: ignore
    if from_remote:
        dir_order = f"{user_host}:{dir_b} {dir_a}"
    else:
        dir_order = f"{dir_a} {user_host}:{dir_b}"
    cmd = f"rsync -auxv{dry_run} {delete} -e ssh {dir_order}" +\
        " --exclude .mypy_cache" + " --exclude __pycache__"
    if print_only:
        logger.info(cmd)
        return "", ""
    else:
        return run_cmd(shlex.split(cmd))


def rsync_over_ssh(user_host: str, dir_a: T_Path, dir_b: Optional[T_Path] = None,
                   delete: bool = False, subdirs: bool = False,
                   from_remote: bool = False, diff: bool = False,
                   dry_run: bool = False, print_only: bool = False):
    """Rsync over `ssh` from `dir_a` to `dir_b`

    Args:
        user_host: user@host
        dir_a: source directory
        dir_b: target directory. If None the same path on target machine is the target
               directory
        delete: Delete also. Equivalent to passing --delete to `rsync`
        subdirs: Instead of source directory, `rsync` each subdirectory in source
                 directory individually. Useful in case the source directory has fewer
                 subdirectories than target and you don't want to overwrite or delete them.
        dry_run: Dry run. Equivalent of option `--dry-run` of `rsync`
        print_only: Only print the rsync command, don't actually do anything.

    """
    logger = logging.getLogger("backup-rsync")
    if diff:
        dry_run = True
        print_only = False
    if subdirs:
        out = {}
        err = {}
        if dir_b is not None:
            raise ValueError("Target directory cannot be given with subdirectories")
        for dir in Path(dir_a).iterdir():
            out[str(dir)], err[str(dir)] = rsync_subr(user_host, dir,
                                                      from_remote=from_remote,
                                                      delete=delete,
                                                      dry_run=dry_run,
                                                      print_only=print_only)
            logger.debug(out[str(dir)])
            splits = out[str(dir)].split("\n")
            if from_remote:
                logger.info(f"From {dir_b} to {dir_a}")
            else:
                logger.info(f"From {dir_a} to {dir_b}")
            logger.info(splits[-3])
            logger.info(splits[-2])
            if err[str(dir)]:
                logger.error(err[str(dir)])
    else:
        out, err = rsync_subr(user_host, dir_a, dir_b=dir_b,
                              from_remote=from_remote,
                              delete=delete,
                              dry_run=dry_run,
                              print_only=print_only)
        if diff:
            logger.info(out)
        else:
            logger.debug(out)
        splits = str(out).split("\n")
        if from_remote:
            logger.info(f"From {dir_b or dir_a} to {dir_a or dir_b}")
        else:
            logger.info(f"From {dir_a or dir_b} to {dir_b or dir_a}")
        if splits[0]:
            logger.info(splits[-3])
            logger.info(splits[-2])
        if err:
            logger.error(err)
    return out, err


def create_logger(logfile: Path, verbosity: str):
    """Create a logger with a given verbosity

    Args:
        logfile: path to logfile
        verbosity: Verbosity of the stream handler

    The verbosity (level) of the logger and the file handler is always DEBUG


    """
    logger = logging.getLogger("backup-rsync")
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    level = getattr(logging, verbosity.upper())
    stream_handler.setLevel(level)
    file_formatter = logging.Formatter(datefmt='%Y/%m/%d %I:%M:%S %p',
                                       fmt="[%(asctime)s] [%(levelname)s] %(message)s")
    stream_formatter = logging.Formatter(fmt="[%(levelname)s] %(message)s")
    stream_handler.setFormatter(stream_formatter)
    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)


def read_config(config_file: Path):
    """Read a yaml config file

    Args:
        config_file: Path to config file


    """
    if config_file.exists():
        with open(Path.home().joinpath(".rsync-backup")) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    else:
        config = None
    return config


def list_and_exit(supported_dirs: Dict[str, T_Path]):
    """Pretty print the supported directories

    Args:
        supported_dirs: Dictionary of dirs and options


    """
    logger = logging.getLogger("backup-rsync")
    import pprint
    if supported_dirs:
        pprint.pprint(supported_dirs)
        sys.exit(0)
    else:
        logger.error("No supported dirs in config")
        sys.exit(1)


def main():
    default_config_file = Path.home().joinpath(".rsync-backup")
    parser = argparse.ArgumentParser()
    parser.add_argument("--dirs", default="", help="Comma separated list of directories to backup")
    parser.add_argument("--targets", default="", help="Comma separated list of target directories")
    parser.add_argument("--list", action="store_true",
                        help="List the supported/configured directories in configuration and exit.")
    parser.add_argument("--exclude-projects", action="store_true",
                        help="Do not backup the projects directory")
    parser.add_argument("--force", action="store_true",
                        help="Force allow --delete option on unsupported directories")
    parser.add_argument("--delete", action="store_true",
                        help="Allow --delete option on unsupported directories")
    parser.add_argument("--no-delete", action="store_true",
                        help="Do not delete even if given in config")
    parser.add_argument("--exclude", type=str, default="",
                        help="Exclude comma separated list of given directories. Useful only when backing up configured directories")
    parser.add_argument("--host", help="Remote host to backup")
    parser.add_argument("--unsupported", action="store_true",
                        help="Run on directories which are not configured." +
                        " Use --list to see currently configured directories")
    parser.add_argument("--root", dest="root_path", default=Path.home(), type=Path,
                        help="Root path from which to consider directories for backup.")
    parser.add_argument("--diff", action="store_true",
                        help="Show only list of files to be updated.")
    parser.add_argument("--from", dest="from_remote", action="store_true",
                        help="Sync from the remote host instead of to.")
    parser.add_argument("--logfile", default=Path.home().joinpath("logs/backup-droid.log"),
                        help="Log file for backup")
    parser.add_argument("--print-only", action="store_true",
                        help="Print the rsync command. Don't do anything not even dry-run.")
    parser.add_argument("--dry-run", action="store_true", help="Dry run.")
    parser.add_argument("-v", "--verbosity", choices=["info", "debug", "warning", "error"],
                        default="info", help="stdout verbosity")
    parser.add_argument("--config-file", default=default_config_file,
                        type=Path, help=f"Path to yaml configuration file. Defaults to $HOME/.rsync_backup")
    args = parser.parse_args()

    config = read_config(args.config_file)
    host = config and config["host"]
    root_path = config and Path(config["root"])
    supported_dirs = config and config["supported_dirs"]
    logfile = Path(os.path.expanduser(args.logfile))
    create_logger(logfile, verbosity=args.verbosity)
    logger = logging.getLogger("backup-rsync")

    if args.list:
        list_and_exit(supported_dirs)

    check_host_given(args, host)
    check_root_path(args, root_path)
    dirs = check_dirs(args, supported_dirs)
    if args.exclude:
        exclude_dirs = args.exclude.split(",")
        for d in exclude_dirs:
            dirs.pop(d)
    targets = args.targets and args.targets.split(",")
    check_delete_flag(args, dirs)

    if not dirs:
        if args.dirs:
            logger.error(f"Need \"--unsupported\" with given directories {args.dirs}")
        else:
            logger.info("Nothing to do here")
    for i, (dir, val) in enumerate(dirs.items()):
        target = None if not targets else targets[i]
        out, err = rsync_over_ssh(host, root_path.joinpath(dir),
                                  dir_b=target,
                                  delete=val["delete"],
                                  subdirs=val.get("subdirs", False),
                                  from_remote=args.from_remote,
                                  diff=args.diff,
                                  dry_run=args.dry_run,
                                  print_only=args.print_only)
        if err:
            logger.error(err)
            return 1
    return 0
