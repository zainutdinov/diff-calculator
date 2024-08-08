from gendiff.parser import read_file


def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = []

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff_lines.append(f"    {key}: {format_value(data1[key])}")
            else:
                diff_lines.append(f"  - {key}: {format_value(data1[key])}")
                diff_lines.append(f"  + {key}: {format_value(data2[key])}")
        elif key in data1:
            diff_lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key in data2:
            diff_lines.append(f"  + {key}: {format_value(data2[key])}")

    return "{\n" + "\n".join(diff_lines) + "\n}"
