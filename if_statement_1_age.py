#!/usr/bin/env python
'''
Возраст

    Попросить пользователя ввести возраст.
    По возрасту определить, чем он должен заниматься: учиться в детском саду,
     школе, ВУЗе или работать.
    Вывести занятие на экран.
'''
# PEP8, global constants should be upper case.
USER_AGE = int(input('Введите возраст: '))
COMMON_STRING = 'Ты должен быть '

if USER_AGE < 7:
    print(COMMON_STRING + 'в детском саду.')
elif USER_AGE < 18:
    print(COMMON_STRING + 'в школе.')
elif USER_AGE < 24:
    print(COMMON_STRING + 'в ВУЗе.')
else:
    print(COMMON_STRING + 'на работе.')
