import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR/'config'/'app_config.yaml'
config_init_path = BASE_DIR/'config'/'access_db.yaml'


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


config = get_config(config_path)
config_init = get_config(config_init_path)
