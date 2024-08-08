import json
import yaml


def read_file(file_path):
    with open(file_path) as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
            return yaml.safe_load(file)
        else:
            raise ValueError('Unsupported file format')
