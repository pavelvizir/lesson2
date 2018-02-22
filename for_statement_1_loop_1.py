#!/usr/bin/env python
'''
Цикл

    Создать список из десяти целых чисел.
    Вывести на экран каждое число, увеличенное на 1.

'''

NUMBERS_LIST = list(range(1, 11))  # 0 - целое, но не натуральное

for number in NUMBERS_LIST:
    print(number + 1)
