from gendiff.diff import generate_diff


def test_generate_diff_json():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'

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


def test_generate_diff_yaml():
    file_path1 = 'tests/fixtures/file1.yaml'
    file_path2 = 'tests/fixtures/file2.yaml'

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


def test_generate_diff_json_stylish():
    file_path1 = 'tests/fixtures/file1_recursion.json'
    file_path2 = 'tests/fixtures/file2_recursion.json'

    diff_result = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

    diff = generate_diff(file_path1, file_path2)

    assert diff == diff_result


def test_generate_diff_yaml_stylish():
    file_path1 = 'tests/fixtures/file1_recursion.yaml'
    file_path2 = 'tests/fixtures/file2_recursion.yaml'

    diff_result = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

    diff = generate_diff(file_path1, file_path2)

    assert diff == diff_result


def test_generate_diff_json_plain():
    file_path1 = 'tests/fixtures/file1_recursion.json'
    file_path2 = 'tests/fixtures/file2_recursion.json'

    diff_result = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From true to null\n"
        "Property 'common.setting4' was added with value: 'blah blah'\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
        "Property 'common.setting6.ops' was added with value: 'vops'\n"
        "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
        "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
        "Property 'group2' was removed\n"
        "Property 'group3' was added with value: [complex value]"
    )

    diff = generate_diff(file_path1, file_path2, format_name='plain')

    assert diff == diff_result


def test_generate_diff_yaml_plain():
    file_path1 = 'tests/fixtures/file1_recursion.yaml'
    file_path2 = 'tests/fixtures/file2_recursion.yaml'

    diff_result = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From true to null\n"
        "Property 'common.setting4' was added with value: 'blah blah'\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
        "Property 'common.setting6.ops' was added with value: 'vops'\n"
        "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
        "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
        "Property 'group2' was removed\n"
        "Property 'group3' was added with value: [complex value]"
    )

    diff = generate_diff(file_path1, file_path2, format_name='plain')

    assert diff == diff_result


def test_generate_diff_json_json():
    file_path1 = 'tests/fixtures/file1_recursion.json'
    file_path2 = 'tests/fixtures/file2_recursion.json'

    diff_result = '''[
  {
    "key": "common",
    "status": "nested",
    "children": [
      {
        "key": "follow",
        "status": "added",
        "value": false
      },
      {
        "key": "setting1",
        "status": "unchanged",
        "value": "Value 1"
      },
      {
        "key": "setting2",
        "status": "removed",
        "value": 200
      },
      {
        "key": "setting3",
        "status": "changed",
        "old_value": true,
        "new_value": null
      },
      {
        "key": "setting4",
        "status": "added",
        "value": "blah blah"
      },
      {
        "key": "setting5",
        "status": "added",
        "value": {
          "key5": "value5"
        }
      },
      {
        "key": "setting6",
        "status": "nested",
        "children": [
          {
            "key": "doge",
            "status": "nested",
            "children": [
              {
                "key": "wow",
                "status": "changed",
                "old_value": "",
                "new_value": "so much"
              }
            ]
          },
          {
            "key": "key",
            "status": "unchanged",
            "value": "value"
          },
          {
            "key": "ops",
            "status": "added",
            "value": "vops"
          }
        ]
      }
    ]
  },
  {
    "key": "group1",
    "status": "nested",
    "children": [
      {
        "key": "baz",
        "status": "changed",
        "old_value": "bas",
        "new_value": "bars"
      },
      {
        "key": "foo",
        "status": "unchanged",
        "value": "bar"
      },
      {
        "key": "nest",
        "status": "changed",
        "old_value": {
          "key": "value"
        },
        "new_value": "str"
      }
    ]
  },
  {
    "key": "group2",
    "status": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  {
    "key": "group3",
    "status": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
]'''

    diff = generate_diff(file_path1, file_path2, format_name='json')

    assert diff == diff_result


def test_generate_diff_yaml_json():
    file_path1 = 'tests/fixtures/file1_recursion.yaml'
    file_path2 = 'tests/fixtures/file2_recursion.yaml'

    diff_result = '''[
  {
    "key": "common",
    "status": "nested",
    "children": [
      {
        "key": "follow",
        "status": "added",
        "value": false
      },
      {
        "key": "setting1",
        "status": "unchanged",
        "value": "Value 1"
      },
      {
        "key": "setting2",
        "status": "removed",
        "value": 200
      },
      {
        "key": "setting3",
        "status": "changed",
        "old_value": true,
        "new_value": null
      },
      {
        "key": "setting4",
        "status": "added",
        "value": "blah blah"
      },
      {
        "key": "setting5",
        "status": "added",
        "value": {
          "key5": "value5"
        }
      },
      {
        "key": "setting6",
        "status": "nested",
        "children": [
          {
            "key": "doge",
            "status": "nested",
            "children": [
              {
                "key": "wow",
                "status": "changed",
                "old_value": "",
                "new_value": "so much"
              }
            ]
          },
          {
            "key": "key",
            "status": "unchanged",
            "value": "value"
          },
          {
            "key": "ops",
            "status": "added",
            "value": "vops"
          }
        ]
      }
    ]
  },
  {
    "key": "group1",
    "status": "nested",
    "children": [
      {
        "key": "baz",
        "status": "changed",
        "old_value": "bas",
        "new_value": "bars"
      },
      {
        "key": "foo",
        "status": "unchanged",
        "value": "bar"
      },
      {
        "key": "nest",
        "status": "changed",
        "old_value": {
          "key": "value"
        },
        "new_value": "str"
      }
    ]
  },
  {
    "key": "group2",
    "status": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  {
    "key": "group3",
    "status": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
]'''

    diff = generate_diff(file_path1, file_path2, format_name='json')

    assert diff == diff_result
