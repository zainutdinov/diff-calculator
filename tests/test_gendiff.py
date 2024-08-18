from gendiff.diff import generate_diff
import pytest


@pytest.mark.parametrize("file_path1, file_path2, expected, format_name", [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/expected_result_1.txt', 'stylish'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'tests/fixtures/expected_result_1.txt', 'stylish'),
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'tests/fixtures/expected_result_2.txt', 'stylish'),
    ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml', 'tests/fixtures/expected_result_2.txt', 'stylish'),
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'tests/fixtures/expected_result_3.txt', 'plain'),
    ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml', 'tests/fixtures/expected_result_3.txt', 'plain'),
    ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'tests/fixtures/expected_result_4.txt', 'json'),
    ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml', 'tests/fixtures/expected_result_4.txt', 'json')
])
def test_generate_diff(file_path1, file_path2, expected, format_name):
    with open(expected, 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2, format_name)
    assert diff == expected_result
