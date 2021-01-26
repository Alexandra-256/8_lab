#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решить индивидуальное задание лабораторной работы 6, оформив каждую команду в виде отдельной функции.
# Условие задания: 18. Использовать словарь, содержащий следующие ключи:
# название товара;
# название магазина,
# в котором продается товар;
# стоимость товара в руб.
# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены в алфавитном порядке по названиям магазинов;
# вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет,
# выдать на дисплей соответствующее сообщение.

import sys

def add(records):
    # Запросить данные о товаре.
    product = input("Название товара: ")
    shop = input("Название магазина: ")
    price = int(input("Стоимость товара: "))

    # Создать словарь.
    record = {
        'product': product,
        'shop': shop,
        'price': price,
    }

    # Добавить словарь в список.
    records.append(record)
    # Отсортировать список в случае необходимости.
    if len(records) > 1:
        records.sort(key=lambda item: item.get('shop', ''))

def show_list(records):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 20,
        '-' * 20,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^20} | {:^20} | {:^20} |'.format(
            "№",
            "Название товара",
            "Название магазина",
            "Стоимость товара"
        )
    )
    print(line)
    # Вывести данные о всех товарах.
    for idx, record in enumerate(records, 1):
        print(
            '| {:>4} | {:<20} | {:<20} | {:>20} |'.format(
                idx,
                record.get('product', ''),
                record.get('shop', ''),
                record.get('price', 0)
            )
        )
        print(line)

def select(records):
    sell = input("Введите название интересующего магазина: ")

    # Инициализировать счетчик.
    count = 0
    # Проверить сведения товара из списка.
    for record in records:
        if record.get('shop') == sell:
            count += 1
            print(
                '{:>4}: {}'.format(count, record.get('product', ''))
            )
    # Если счетчик равен 0, то магазин не найден.
    if count == 0:
        print("Магазин с таким названием не найден.")

def help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить товары;")
    print("list - вывести список товаров;")
    print("select - запросить товары в выбранном магазине;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

if __name__ == '__main__':
    # Запись.
    records = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            add(records)
        elif command == 'list':
            show_list(records)
        elif command.startswith('select'):
            select(records)
        elif command == 'help':
            help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)