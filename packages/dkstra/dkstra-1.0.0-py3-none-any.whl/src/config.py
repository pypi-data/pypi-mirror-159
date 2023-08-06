import collections.abc
import os
import re
from typing import Dict, Any, List, Optional
import pathlib

import yaml
from box import Box


def _yaml_parse_environ(yaml_module):
    """Used to parse expressions of the form << ENVIRON_VARIABLE >> in YAML files.
    For more information, see: http://stackoverflow.com/a/27232341
    """
    pattern = re.compile(r"^(.*)\<\<(.*)\>\>(.*)$")
    yaml_module.add_implicit_resolver("!pathex", pattern)

    def pathex_constructor(loader, node):
        value = loader.construct_scalar(node)
        left, env_var, right = pattern.match(value).groups()
        env_var = env_var.strip()
        if env_var not in os.environ:
            msg = f"Environment variable {env_var} not defined"
            raise ValueError(msg)
        return left + os.environ[env_var] + right

    yaml_module.add_constructor("!pathex", pathex_constructor)

    return yaml_module


def join_path(loader, node):
    """Custom handler to join strings in YAML files"""
    seq = loader.construct_sequence(node)
    return os.path.join(*[str(i) for i in seq])


# Add the functionality to parse environment variables to YAML module
yaml = _yaml_parse_environ(yaml)
# Add the functionality to join strings to YAML module
yaml.add_constructor("!path", join_path)


def load_config(config_filename: str) -> Box:
    """Return a dictionary with the settings file in the file *path*."""
    with open(config_filename) as f:
        settings = Box(yaml.load(f, Loader=yaml.Loader))
    return settings


def merge(old: Dict[Any, Any], new: Dict[Any, Any]) -> Box:
    """
    Merge the two dictionaries together into a single dictionary.
    Priority will go to the ``new`` dictionary object when the same
    key exists in both of the dictionaries.
    Parameters
    ----------
    old:
        Dictionary to merge the new values into
    new:
        Dictionary to merge into the old dictionary
    Returns
    -------
    :
        Merged dictionary containing values from both of the dictionaries
    """
    for k, v in new.items():
        if isinstance(old, collections.abc.Mapping):
            if isinstance(v, collections.abc.Mapping):
                old[k] = merge(old.get(k, {}), v)
            else:
                old[k] = v
        else:
            old = {k: v}

    return Box(old)


def load_yaml_files(paths: List[str]) -> Dict[str, Any]:
    """
    Loads a list of yaml files and returns a single dictionary
    containing all of them. Note that files listed later in the list
    will have higher precedence since they may potentially overwrite
    values of yaml files loaded in before them in the list.
    This function is named ``raw`` since the ``load_yaml_files`` function
    performs additional steps on top of loading in the raw yaml files.
    Parameters
    ----------
    paths:
        List of absolute file paths to load
    Returns
    -------
    :
        Merged dictionary containing the config values
    """
    res = {}
    for p in paths:
        config = load_config(p)
        config_name = pathlib.Path(p).stem
        config = {config_name: config}
        res = merge(res, load_config(p))
    return res


def get_config_files_in_dir(dir_path: str) -> List[Optional[pathlib.Path]]:
    """
    Get a list of yaml config files (*.yaml, *.yml) that are in
    the given directory.
    Parameters
    ----------
    dir_path:
        Path to the directory to search under
    Returns
    -------
    :
        List of yaml config files in the directory
    """
    path = pathlib.Path(dir_path)
    types = ("*.yml", "*.yaml")
    config_files = []
    for files in types:
        config_files.extend(path.rglob(files))
    return config_files


def resolve_paths(input_dict: dict) -> dict:
    """
    Resolves paths in config by concatenating all the sub-folders. For example
    output_files: [<< DATA >>, output_folder, filename.csv] will become
    << DATA >>/output_folder/filename.csv
    where << DATA >> is the environment variable pointing to the root path
    Parameters
    ----------
    input_dict: input dictionary

    Returns
    -------

    """
    for k in input_dict.keys():
        if isinstance(input_dict[k], list):
            input_dict[k] = os.path.join(*input_dict[k])
        else:
            input_dict[k] = resolve_paths(input_dict[k])
    return input_dict


def resolve_references(input_dict: dict, config: dict) -> dict:
    """
    Substitutes the references with the values specified in the dictionary
    Parameters
    ----------
    input_dict
    config

    Returns
    -------

    """
    for k in input_dict.keys():
        if isinstance(input_dict[k], str):
            path_token = re.findall(r"{(.*?)}", input_dict[k])
            for p in path_token:
                input_dict[k] = input_dict[k].replace(
                    "{" + p + "}", eval(f"config.{p}")
                )
        else:
            input_dict[k] = resolve_references(input_dict[k], config)
    return input_dict


def load_configs(path: str) -> Box:
    """
    This function loads a set of configs from a folder. It will create a single dictionary with all the configs
    appended. For example if we have
    - config1.yaml
    - config2.yaml
    - config3.yaml
    The output will be the following Box object:
    {
        "config1": config_1_dict
        "config2": config_2_dict
        "config3": config_3_dict
    }
    Parameters
    ----------
    path

    Returns
    -------

    """
    if isinstance(path, str):
        path = [path]

    files = []
    for p in path:
        if os.path.isdir(p):
            files.extend(get_config_files_in_dir(p))
        else:
            files.append(p)

    config = Box(load_yaml_files(files))
    if "datasets" in config:
        config.datasets = resolve_paths(config.datasets)
        if "project_paths" in config.datasets:
            config.datasets = resolve_references(config.datasets, config)

    return config
