#!/usr/bin/env python
'''
Задание

    1. Пройдите в цикле по списку
    ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
     пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся".
     Подсказка: используйте метод list.pop()
    2. Перепишите предыдущий пример в виде функции find_person(name),
     которая ищет имя в списке.
    3. Написать функцию ask_user() чтобы с помощью input() спрашивать
     пользователя “Как дела?”, пока он не ответит “Хорошо”
    4. При помощи функции get_answer() отвечать на вопросы пользователя в
     ask_user(), пока он не скажет “Пока!”

'''

NAMES = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
NAME = "Валера"


def find_person(name):
    ''' Ищем циклом имя в списке. '''
    names_copy = NAMES[:]

    while names_copy:
        if names_copy.pop() == name:
            print(name + ' нашёлся.')

            break

    else:
        print(name + ' не нашёлся.')


find_person(NAME)


def ask_user():
    ''' Ask until get desired result. '''

    while True:
        question = input("Скажи что-нибудь\n")
        if question == "Пока!":
            print('До встречи!')
            break
        else:
            print(get_answer(question, answers))


# Последнее задание про get_answer() не понял
# кто у кого что спрашивает и какой ответ выдавать...

answers = {"привет": "И тебе привет!",
           "как дела": "Лучше всех!",
           "пока": "Увидимся."}


def get_answer(question, answers):
    return answers.get(question.lower(), "Не могу ответить :-(")

ask_user()