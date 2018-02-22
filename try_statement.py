#!/usr/bin/env python
'''
Задание

    1. Переписать функцию ask_user(), добавив обработку exception-ов
    2. Добавить перехват ctrl+C и прощание

'''

# Садистская версия :-)


def ask_user():
    ''' Ask until get desired result. '''

    while True:
        try:
            if str(input("Как дела? ")) == "Хорошо":
                break
        except KeyboardInterrupt:
            print(' Отвечай нормально!')

    print('Пока!')


ask_user()
