#!/usr/bin/env python
'''
Сравнение строк

    Написать функцию, которая принимает на вход две строки.
    Если строки одинаковые, возвращает 1.
    Если строки разные и первая длиннее, возвращает 2.
    Если строки разные и вторая строка 'learn', возвращает 3.

'''


def compare_two_strings(string_1, string_2):
    ''' Obvious doc_string. '''

    if string_1 == string_2:
        return 1
    elif len(string_1) > len(string_2):
        return 2
    elif string_2 == 'learn':
        return 3

    return 4  # Не хочется иметь что-то необработанное


STRING_1 = str(input('Введите первую строку: '))
STRING_2 = str(input('Введите вторую строку: '))
print(compare_two_strings(STRING_1, STRING_2))
