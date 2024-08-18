def format_value_stylish(value, depth):
    indent = '    ' * depth
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value_stylish(v, depth + 1)}")
        result = "\n".join(lines)
        return f"{{\n{result}\n{indent}}}"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def format_nested(key, item, depth):
    nested_value = format_stylish(item['children'], depth + 1)
    return f"{'    ' * (depth - 1)}    {key}: {nested_value}"


def format_unchanged(key, item, depth):
    return f"{'    ' * (depth - 1)}    {key}: {format_value_stylish(item['value'], depth)}"


def format_added(key, item, depth):
    return f"{'    ' * (depth - 1)}  + {key}: {format_value_stylish(item['value'], depth)}"


def format_removed(key, item, depth):
    return f"{'    ' * (depth - 1)}  - {key}: {format_value_stylish(item['value'], depth)}"


def format_changed(key, item, depth):
    old_value = format_value_stylish(item['old_value'], depth)
    new_value = format_value_stylish(item['new_value'], depth)
    return [
        f"{'    ' * (depth - 1)}  - {key}: {old_value}",
        f"{'    ' * (depth - 1)}  + {key}: {new_value}"
    ]


def format_stylish(diff, depth=1):
    lines = []

    for item in diff:
        key = item['key']
        status = item['status']

        match status:
            case "nested":
                lines.append(format_nested(key, item, depth))
            case "unchanged":
                lines.append(format_unchanged(key, item, depth))
            case "added":
                lines.append(format_added(key, item, depth))
            case "removed":
                lines.append(format_removed(key, item, depth))
            case "changed":
                lines.extend(format_changed(key, item, depth))
            case _:
                raise ValueError(f"Unsupported status '{status}' in diff structure")

    return "{\n" + "\n".join(lines) + f"\n{'    ' * (depth - 1)}}}"
