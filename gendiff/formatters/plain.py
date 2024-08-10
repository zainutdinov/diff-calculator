def format_value_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def build_plain(diff, path=''):
    result = []
    for item in diff:
        key = item['key']
        status = item['status']
        full_path = f"{path}.{key}" if path else key

        match status:
            case "nested":
                result.extend(build_plain(item['children'], full_path))
            case "added":
                value = format_value_plain(item['value'])
                result.append(f"Property '{full_path}' was added with value: {value}")
            case "removed":
                result.append(f"Property '{full_path}' was removed")
            case "changed":
                old_value = format_value_plain(item['old_value'])
                new_value = format_value_plain(item['new_value'])
                result.append(f"Property '{full_path}' was updated. From {old_value} to {new_value}")
            case "unchanged":
                continue
    return result


def format_plain(diff):
    return "\n".join(build_plain(diff))
