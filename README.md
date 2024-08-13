<div align="center">
<h1>Вычислитель отличий</h1>
</div>


### Hexlet tests and linter status:
[![Actions Status](https://github.com/zainutdinov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/zainutdinov/python-project-50/actions)

### CodeClimate Badges
[![Maintainability](https://api.codeclimate.com/v1/badges/0abd02f71d6a9cbb2ddb/maintainability)](https://codeclimate.com/github/zainutdinov/python-project-50/maintainability)

### Test Coverage Badge
[![Test Coverage](https://api.codeclimate.com/v1/badges/0abd02f71d6a9cbb2ddb/test_coverage)](https://codeclimate.com/github/zainutdinov/python-project-50/test_coverage)

### Python CI Badge
[![Python CI](https://github.com/zainutdinov/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/zainutdinov/python-project-50/actions/workflows/pyci.yml)


## Описание проекта

**«Вычислитель отличий»** — программа, которая определяет разницу между двумя структурами данных.

Возможности утилиты:

- Поддержка разных входных форматов: yaml, json
- Генерация отчета в виде plain text, stylish и json

## Требования

- python ^3.12
- pyyaml ^6.0.2

## Инструкция по установке

#### Python

> Перед установкой пакета убедитесь, что у вас установлен Python версии 3.12 или выше:

```bash
python --version
# Python 3.12.0+
```
#### Poetry

> Проект использует менеджер зависимостей Poetry. Для установки Poetry используйте его [официальную инструкцию](https://python-poetry.org/docs/#installation).


### Установка пакета

> Чтобы использовать пакет, вам нужно скопировать репозиторий на свой компьютер. Это делается с помощью команды ``git clone``:

```bash
git clone https://github.com/zainutdinov/python-project-50
```

> Далее выполните установку пакета:

```bash
cd python-project-50
```

```bash
poetry build
python3 -m pip install --user dist/*.whl
```


## Запуск программы

> Для программы игры используйте команду:
```bash
gendiff first_file second_file
```
где "first_file, second_file" - пути до файлов, которые сравнивает программа

> Пример запуска программы:
[![asciicast](https://asciinema.org/a/g5KTE8N8itQsD6NWkPT62CB7x.svg)](https://asciinema.org/a/g5KTE8N8itQsD6NWkPT62CB7x)


#### По умолчанию программа работает с форматтером "stylish"
##### Форматтер работает по флагу -f, --format (подробнее в справке -h, --help)

> Пример запуска программы с форматтером "stylish":
```bash
gendiff tests/fixtures/file1_recursion.json tests/fixtures/file2_recursion.json
```
```bash
gendiff -f stylish tests/fixtures/file1_recursion.json tests/fixtures/file2_recursion.json
```
[![asciicast](https://asciinema.org/a/MA3g6HDYnF2ASaARjW5jEo24g.svg)](https://asciinema.org/a/MA3g6HDYnF2ASaARjW5jEo24g)


#### Форматтер "plain"

> Пример запуска программы с форматтером "plain":
```bash
gendiff -f plain tests/fixtures/file1_recursion.json tests/fixtures/file2_recursion.json
```
[![asciicast](https://asciinema.org/a/4eAk4MM1scGFaCIYy6N0NTXKF.svg)](https://asciinema.org/a/4eAk4MM1scGFaCIYy6N0NTXKF)


#### Форматтер "json"

> Пример запуска программы с форматтером "json":
```bash
gendiff -f json tests/fixtures/file1_recursion.json tests/fixtures/file2_recursion.json
```
[![asciicast](https://asciinema.org/a/HDvF4krQDdZKu3EjS5b48nnnn.svg)](https://asciinema.org/a/HDvF4krQDdZKu3EjS5b48nnnn)