import src.tasks as tasks
from src.logging import get_logger
from src.config import load_configs
import click


@click.command()
@click.option('--task_name', type=str)
@click.option('--config', type=str)
@click.option('--log', type=str)
def run(
    task_name: str, config: str = None, log: str = None
):
    """
    This is the main entry point of the project, a wrapper function that runs a specific task called under string and
    adds config and constants. Any task that is called has to be imported in the __init__.py of the corresponding module
    Parameters
    ----------
    task_name: main that will be called by the run function
    config: path for the config of the pipeline
    log: path of the log for the pipeline

    Returns
    Nothing
    -------

    """
    settings_run = dict()
    if config:
        settings_run["config"] = load_configs(config)

    if log:
        settings_run["log"] = get_logger(log)

    main_function = getattr(tasks, task_name)
    main_function(**settings_run)


if __name__ == "__main__":
    run()
