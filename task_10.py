#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 10. Решите следующую задачу: напишите функцию, которая считывает с клавиатуры числа и
# перемножает их до тех пор, пока не будет введен 0. Функция должна возвращать
# полученное произведение. Вызовите функцию и выведите на экран результат ее работы.

def function():
    while True:
        g = 1
        n = float(input("Введите число n: "))
        k = float(input("Введите число k: "))

        if n == 0 or k == 0:
            print("Работа функции прекращена.")
            return function

        g *= n
        g *= k
        print(f"Результат умножения: {g}")

if __name__ == '__main__':

    function()