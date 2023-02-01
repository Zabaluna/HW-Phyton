# 4 Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

# создаем словарь: ключ значение ( от 0 до 100)
def create_dictionary():
    degree = int(input('Enter the k - degree:'))
    my_dict ={}
    for n in range(degree, -1, -1):
        my_dict[n] = random.randint(0,101)
    return my_dict

# my_dict = create_dictionary()
# print(my_dict)

# создаем многочлен
def polynomial(my_dict:dict) -> str:
    new_equation = []
    for key, value in my_dict.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' + '.join(new_equation) + ' = 0'
    # new_equation = new_equation.replace('+-', '-'), тк от 0 до 100 будет только плюс
    new_equation = new_equation.replace(' 1*x', ' x')
    new_equation = new_equation.replace('*x**0', '')
    new_equation = new_equation.replace('x**1', 'x')
    return new_equation

# new_equation=polynomial(my_dict)
# print(new_equation)

def main():

    my_dict = create_dictionary()
    print(my_dict)

    new_equation1=polynomial(my_dict)
    print(new_equation1)

    # записываем наш многчлен в файл
    with open("D:\GB\PYTHON\Seminar4\HOMEWORK\\new_equation_k.txt", "w", encoding='UTF-8') as filek:
        filek.write(new_equation1)
    

if __name__ == "__main__":
    main()    

    
#  def general_koef(n):

#     mnogochlen = ""
        
#     for i in range(n, -1, -1):
#         rnd = randint(0,10)
#         if rnd != 0:
#             if len(mnogochlen) > 1:
#                 mnogochlen += " + "
#             if i == 0:
#                 mnogochlen += str(rnd)
#             else:
#                 mnogochlen += str(rnd) + "*x^" + str(i)
#     mnogochlen += " = 0"
#     return mnogochlen


import random
from os import system

system("cls")

k = int(input('Enter degree of number: '))

polynominal = ''
for i in range(k, 0, -1):
    polynominal += str(random.randrange(0,101))+'*x^' + str(i) + ' + '
polynominal += str(random.randrange(0,101)) + ' = 0'
print(polynominal)

with open('polynominal.txt', "w") as f_obj:
    print(polynominal, file=f_obj, end='')


import random

sum = int(input('Input K: '))

print(f'k = {sum} -> ', end = '')
null_elems = 0
for i in range(sum,-1,-1):    
    num = random.randint(0,100)
    
    if num == 0: #проверка на необходимость знака '+' при пустых первых значениях
        null_elems += 1
        continue
    plus = ' + ' if sum - null_elems != i else ''
        
    if i == sum:
        print(f'{num}*x^{i}', end = '')
    elif i != 0: 
        print(f'{plus}{num}*x^{i}', end = '')
    elif i == 1: 
        print(f'{plus}{num}*x', end = '')
    else:
        print(f'{plus}{num}', end = '')
        
print(' = 0')
