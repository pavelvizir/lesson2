#!/usr/bin/env python
'''
Цикл

    Ввести с клавиатуры строку.
    Вывести эту же строку вертикально: по одному символу на строку консоли.

'''

STRING = str(input('Введите строку: '))

for letter in list(STRING):
    print(letter)
