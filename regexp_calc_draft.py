
from re import fullmatch,search
a = '3/4 +6**2-6*4  -123 +6*3**---2//4 +100/55='
b = '3/4 +6**2-6*4/  0  -123 +6*3**2/4 +100/0='
c = ''
def calc(c):
	if fullmatch(r'[0-9\/\*\-\+\ ]+',c[:-1]) and not search(r'\/\s*0',c[:-1]) and c[-1] == '=':
		print(eval(c[:-1]))
	else:
		print('Wrong request!')
	
calc(a)
calc(b)
calc(c)

#3.25
#Wrong request!
#Wrong request!
#[Program finished]

#brackets need exceptiob zero
# хотя можно и вычислять то, что в кобках..., если цель без эксепшнов
# через стэк самые вложенные скобки
# или рег группами о.о
#parenthisis check for balanced
#zapretit sosedstvo (*, +), но оставить (-

#add parsing %
#any ----at the end of operation
#allow **, //
#forbid any other 2symbol
#make it decimal
#separate errors in other ifs

#test with random generated
#похоже, что решение через евал не легче, т.к. сменили сложность вычислений на сложность проверки

def do_parentheses_match(input_string):
    s = []
    balanced = True
    index = 0
    while index < len(input_string) and balanced:
        token = input_string[index]
        if token == "(":
            s.append(token)
        elif token == ")":
            if len(s) == 0:
                balanced = False
            else:
                s.pop()

        index += 1

    return balanced and len(s) == 0
    
    