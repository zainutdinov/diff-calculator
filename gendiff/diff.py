from gendiff.parser import read_file
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def process_both_dicts(key, data1, data2):
    if isinstance(data1[key], dict) and isinstance(data2[key], dict):
        children = build_diff(data1[key], data2[key])
        return {
            'key': key,
            'status': 'nested',
            'children': children
        }
    elif data1[key] == data2[key]:
        return {
            'key': key,
            'status': 'unchanged',
            'value': data1[key]
        }
    else:
        return {
            'key': key,
            'status': 'changed',
            'old_value': data1[key],
            'new_value': data2[key]
        }


def process_only_in_first(key, data1):
    return {
        'key': key,
        'status': 'removed',
        'value': data1[key]
    }


def process_only_in_second(key, data2):
    return {
        'key': key,
        'status': 'added',
        'value': data2[key]
    }


def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key in data1 and key in data2:
            diff.append(process_both_dicts(key, data1, data2))
        elif key in data1:
            diff.append(process_only_in_first(key, data1))
        elif key in data2:
            diff.append(process_only_in_second(key, data2))

    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)
    if format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    return format_stylish(diff)
