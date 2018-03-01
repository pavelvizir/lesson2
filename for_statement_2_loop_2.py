#!/usr/bin/env python
'''
Цикл

    Ввести с клавиатуры строку.
    Вывести эту же строку вертикально: по одному символу на строку консоли.

'''


def vertical_string():
    ''' obvious doc_string '''

    string = input('Введите строку: ')

    for letter in string:
        print(letter)


vertical_string()
