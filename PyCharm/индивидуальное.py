#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def help1():
    """"
    Функция для вывода списка команд
    """
    # Вывести справку о работе с программой.
    print("Список команд:")
    print("add - добавить информацию;")
    print("list - вывести список ;")
    print("select <тип> - вывод на экран фамилия, имя; знак Зодиака; дата рождения ")
    print("help - отобразить справку;")
    print("load - загрузить данные из файла;")
    print("save - сохранить данные в файл;")
    print("exit - завершить работу с программой.")


def add1():
    """"
    Функция для добавления информации о новых рейсах
    """
    # Запросить данные о работнике.
    name = input("Фамилия и инициалы? ")
    post = input("знак зодиака? ")
    year = int(input("Год рождения? "))
    # Создать словарь.
    i = {
        'name': name,
        'знак зодиака': post,
        'year': year,
    }

    return i


def error1(command):
    """"
    функция для неопознанных команд
    """
    print(f"Неизвестная команда {command}")


def list(worcer):
    """"
    Функция для вывода списка добавленных рейсов
    """
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)

    # Вывести данные о всех сотрудниках.
    for idx, i in enumerate(worcer, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                i.get('name', ''),
                i.get('знак зодиака', ''),
                i.get('year', 0)
            )
        )
    print(line)


def validate_json_data(data):

    schema = {
    "title": "worcer",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "number": {"type": "integer"},
            "tip": {"type": "string"}
        },
        "additionalProperties": False,
        "required": ["name", "знак зодиака", "year"]
    }
}

    try:
        jsonschema.validate(data, schema)
        print("Данные прошли валидацию.")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print("Ошибка валидации данных:", e)
        return False

def save_workers(file_name, staff):
    """
    Сохранить всех работников в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кириллицы установим ensure_ascii=False
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_workers(file_name):
    """
    Загрузить всех работников из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        n = json.load(fin)
        if validate_json_data(n):
            return n
        else:
            return False

def select(command, worcer):
    """""
    Функция для получения номера рейса и пункта назначения по заднному типу самолёта.
    """
    # Разбить команду на части для выделения номера года.
    parts = command.split(' ', maxsplit=1)
    # Проверить сведения работников из списка.
    count = 0

    for i in worcer:
        for k, v in i.items():

            if v == parts[1]:
                print("Имя - ", i["name"])
                print("Знак зодиака - ", i["post"])
                count += 1
    # Если счетчик равен 0, то работники не найдены.

    if count == 0:
        print("человек с заланным знаком зодиака не найден.")


def main1():
    """"
    Главная функция программы.
    """
    print("Список команд:\n")
    print("add - добавить рейс;")
    print("list - вывести список рйсов;")
    print("select <тип> - вывод на экран пунктов назначения и номеров рейсов для данного типа самолёта")
    print("select <стаж> - запросить работников со стажем;")
    print("help - отобразить справку;")
    print("load - загрузить данные из файла;")
    print("save - сохранить данные в файл;")
    print("exit - завершить работу с программой.")
    # Список работников.
    worcer = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.

        if command == 'exit':
            break

        elif command == 'add':
            # Добавить словарь в список.
            i = add1()
            worcer.append(i)
            # Отсортировать список в случае необходимости.
            if len(worcer) > 1:
                worcer.sort(key=lambda item: item.get('name', ''))

        elif command.startswith("save "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]

            # Сохранить данные в файл с заданным именем.
            save_workers(file_name, worcer)

        elif command.startswith("load "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]

            # Сохранить данные в файл с заданным именем.
            worcer = load_workers(file_name)

        elif command == 'list':
            list(worcer)

        elif command.startswith('select '):
            select(command, worcer)

        elif command == 'help':
            help1()

        else:
            error1("command")


if __name__ == '__main__':
    main1()