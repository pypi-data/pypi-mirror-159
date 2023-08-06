from typing import Dict, Tuple, List
import os
from dotenv import load_dotenv
from src.logging import get_logger
from src.config import load_configs
from box import Box
import logging
import pathlib


def initialize_run(dict_vars: Dict = None) -> Tuple[Box, logging.log]:
    """
    Initializes a run merging the dictionaries from the config path and the region specific path
    Returns:

    """
    import src

    path_init = src.__file__
    path_repo = os.path.abspath(os.path.join(path_init, os.pardir, os.pardir))
    os.environ["REPO"] = path_repo
    path_config = os.path.join(path_repo, "src", "configs")
    load_dotenv(os.path.join(path_repo, "environment.env"), override=True)
    if dict_vars is not None:
        for var in dict_vars:
            os.environ[var] = dict_vars[var]
    log = get_logger(os.path.join(os.environ["LOG"]))
    config = load_configs(os.path.join(path_config))
    create_directories(config.datasets.project_paths)

    return config, log


def create_directories(project_paths: List[str]) -> None:
    """
    Generates the directories structure of each run of the project according to the config file, the current setup is:
    date
    ├── data
    │   ├── raw
    │   ├── clean
    ├── logs
    ├── output
    Parameters
    ----------
    project_paths

    Returns Nothing, creates a set of directories according to a dictionary structure
    -------

    """
    # -----Create all directoreies in list ---- #
    for path_name in project_paths:
        pathlib.Path(path_name).mkdir(parents=True, exist_ok=True)