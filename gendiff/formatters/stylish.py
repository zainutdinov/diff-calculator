def format_value(value, depth):
    indent = '    ' * depth
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        result = "\n".join(lines)
        return f"{{\n{result}\n{indent}}}"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def format_stylish(diff, depth=1):
    indent = '    ' * (depth - 1)
    lines = []

    for item in diff:
        key = item['key']
        status = item['status']
        if status == "nested":
            nested_value = format_stylish(item['children'], depth + 1)
            lines.append(f"{indent}    {key}: {nested_value}")
        elif status == "unchanged":
            lines.append(f"{indent}    {key}: {format_value(item['value'], depth)}")
        elif status == "added":
            lines.append(f"{indent}  + {key}: {format_value(item['value'], depth)}")
        elif status == "removed":
            lines.append(f"{indent}  - {key}: {format_value(item['value'], depth)}")
        elif status == "changed":
            lines.append(f"{indent}  - {key}: {format_value(item['old_value'], depth)}")
            lines.append(f"{indent}  + {key}: {format_value(item['new_value'], depth)}")

    return "{\n" + "\n".join(lines) + f"\n{indent}}}"
