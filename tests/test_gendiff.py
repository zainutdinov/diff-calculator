from gendiff.diff import generate_diff


def test_generate_diff_json():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/expected_result_1.txt', 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == expected_result


def test_generate_diff_yaml():
    file_path1 = 'tests/fixtures/file1.yaml'
    file_path2 = 'tests/fixtures/file2.yaml'
    with open('tests/fixtures/expected_result_1.txt', 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == expected_result


def test_generate_diff_json_stylish():
    file_path1 = 'tests/fixtures/file1_recursion.json'
    file_path2 = 'tests/fixtures/file2_recursion.json'
    with open('tests/fixtures/expected_result_2.txt', 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == expected_result


def test_generate_diff_yaml_stylish():
    file_path1 = 'tests/fixtures/file1_recursion.yaml'
    file_path2 = 'tests/fixtures/file2_recursion.yaml'
    with open('tests/fixtures/expected_result_2.txt', 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2)
    assert diff == expected_result


def test_generate_diff_json_plain():
    file_path1 = 'tests/fixtures/file1_recursion.json'
    file_path2 = 'tests/fixtures/file2_recursion.json'
    with open('tests/fixtures/expected_result_3.txt', 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2, format_name='plain')
    assert diff == expected_result


def test_generate_diff_yaml_plain():
    file_path1 = 'tests/fixtures/file1_recursion.yaml'
    file_path2 = 'tests/fixtures/file2_recursion.yaml'
    with open('tests/fixtures/expected_result_3.txt', 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2, format_name='plain')
    assert diff == expected_result


def test_generate_diff_json_json():
    file_path1 = 'tests/fixtures/file1_recursion.json'
    file_path2 = 'tests/fixtures/file2_recursion.json'
    with open('tests/fixtures/expected_result_4.txt', 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2, format_name='json')
    assert diff == expected_result


def test_generate_diff_yaml_json():
    file_path1 = 'tests/fixtures/file1_recursion.yaml'
    file_path2 = 'tests/fixtures/file2_recursion.yaml'
    with open('tests/fixtures/expected_result_4.txt', 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2, format_name='json')
    assert diff == expected_result
