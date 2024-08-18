import json
import yaml


def parse_file(file, extension):
    if extension == '.json':
        return json.load(file)
    elif extension == '.yml' or '.yaml':
        return yaml.safe_load(file)
    else:
        raise ValueError('Unsupported file format')


def read_file(file_path):
    with open(file_path) as file:
        extension = file_path[file_path.rfind('.'):]
        return parse_file(file, extension)
