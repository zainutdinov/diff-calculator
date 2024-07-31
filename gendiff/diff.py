import json


def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"    {key}: {format_value(data1[key])}")
            else:
                diff.append(f"  - {key}: {format_value(data1[key])}")
                diff.append(f"  + {key}: {format_value(data2[key])}")
        elif key in data1:
            diff.append(f"  - {key}: {format_value(data1[key])}")
        elif key in data2:
            diff.append(f"  + {key}: {format_value(data2[key])}")

    return "{\n" + "\n".join(diff) + "\n}"
