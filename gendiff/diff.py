from gendiff.parser import read_file
from gendiff.formatters.stylish import format_stylish


def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                children = build_diff(data1[key], data2[key])
                diff.append({
                    'key': key,
                    'status': 'nested',
                    'children': children
                })
            elif data1[key] == data2[key]:
                diff.append({
                    'key': key,
                    'status': 'unchanged',
                    'value': data1[key]
                })
            else:
                diff.append({
                    'key': key,
                    'status': 'changed',
                    'old_value': data1[key],
                    'new_value': data2[key]
                })
        elif key in data1:
            diff.append({
                'key': key,
                'status': 'removed',
                'value': data1[key]
            })
        elif key in data2:
            diff.append({
                'key': key,
                'status': 'added',
                'value': data2[key]
            })

    return diff


def generate_diff(file_path1, file_path2, formatter=format_stylish):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    
    diff = build_diff(data1, data2)
    return formatter(diff)
