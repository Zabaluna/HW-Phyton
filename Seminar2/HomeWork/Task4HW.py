# 4 Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt
#  в одной строке одно число.

import random

num = int(input("Ведите число: "))  # = 5
my_list = []
for i in range(num):
    my_list.append(random.randint(-num, num))
print(my_list)
# делали так на 1й задаче 2го семинара

path = 'file.txt'
data = open(path, 'w')
data.write('2\n')
data.write('4\n')
data.close()

path = 'file.txt'
data = open(path, 'r')
mult = 1
for line in data:
    mult*=my_list[int(line)]
    # print(line, end='')
print(mult)   

