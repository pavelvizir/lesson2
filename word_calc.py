#!/usr/bin/env python
from operator import add, mul

str1 = 'один и три плюс на два и один'
lst1 = str1.split()
numbers = {'один': 1, 'два': 2}
operators = {'плюс': add, 'умножить': mul}

lst2 = []
i = 0

while i < len(lst1):
    if len(lst2) < 1:
        if lst1[i] in numbers.keys():
            lst2.append(numbers[lst1[i]])
    elif len(lst2) < 2:
        if lst1[i] == 'и':
            if lst1[i + 1] in numbers.keys():
                lst2[0] = lst2[0] + numbers[lst1[i + 1]] / 10
                i += 2

                continue
        elif lst1[i] in operators.keys():
            lst2.append(operators[lst1[i]])
    elif len(lst2) < 3:
        if lst1[i] in numbers.keys():
            lst2.append(numbers[lst1[i]])
    else:
        if lst1[i] == 'и':
            if lst1[i + 1] in numbers.keys():
                lst2[2] = lst2[2] + numbers[lst1[i + 1]] / 10
    i += 1

print(lst2)
print(lst2[1](lst2[0], lst2[2]))
