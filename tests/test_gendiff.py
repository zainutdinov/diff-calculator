from gendiff.diff import generate_diff


def test_generate_diff():
    file_path1 = 'tests/file1.json'
    file_path2 = 'tests/file2.json'

    diff_result = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

    diff = generate_diff(file_path1, file_path2)

    assert diff == diff_result
