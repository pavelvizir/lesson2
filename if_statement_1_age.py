#!/usr/bin/env python
'''
Возраст

    Попросить пользователя ввести возраст.
    По возрасту определить, чем он должен заниматься: учиться в детском саду,
     школе, ВУЗе или работать.
    Вывести занятие на экран.
'''


def age_tell_what_to_do():
    user_age = int(input('Введите возраст: '))
    common_string = 'Ты должен быть '

    if user_age < 7:
        print(common_string + 'в детском саду.')
    elif user_age < 18:
        print(common_string + 'в школе.')
    elif user_age < 24:
        print(common_string + 'в ВУЗе.')
    else:
        print(common_string + 'на работе.')


age_tell_what_to_do()
