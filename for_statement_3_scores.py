#!/usr/bin/env python
'''
Оценки

    Создать список с оценками учеников разных
     классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
    Посчитать и вывести средний балл по всей школе.
    Посчитать и вывести средний балл по каждому классу.

'''

from statistics import mean


def print_classes_mean_scores():
    ''' dummy doc_string '''

    school_classes_scores = [
        {
            'school_class': '4a',
            'scores': [3, 4, 4, 5, 2]
        },
        {
            'school_class': '4b',
            'scores': [5, 4, 3, 5, 2]
        },
        {
            'school_class': '5a',
            'scores': [3, 4, 4, 5, 4]
        },
        {
            'school_class': '5b',
            'scores': [4, 2, 4, 5, 2]
        },
        {
            'school_class': '6a',
            'scores': [3, 5, 4, 5, 3]
        },
        {
            'school_class': '6b',
            'scores': [2, 4, 4, 3, 5]
        },
    ]

    # Общий бал для школы созданием списка в цикле ниже
    #  показался совсе некрасивым. Переделал.
    print('Средний балл по школе: ' + str(
        mean([
            score for school_class in school_classes_scores
            for score in school_class['scores']
        ])))

    for school_class in school_classes_scores:
        print('Средний балл в классе "{}": {}'.format(
            str(school_class['school_class']), str(
                mean(school_class['scores']))))


print_classes_mean_scores()
