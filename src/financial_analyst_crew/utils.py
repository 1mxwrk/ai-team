import yaml

def get_config(config_file_name):
    cfg = {}
    with open(config_file_name, "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return cfg