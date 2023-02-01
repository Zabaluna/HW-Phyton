# 3 Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


num = int(input("Ведите число: ")) # = 5
my_list = []
for i in range(num):
    my_list.append(random.uniform(0.00, 100.99))
    my_list[i]=round(my_list[i],2)
print(f'{my_list} -->')

my_new_list = [round(i%1,2) for i in my_list if i%1 != 0]
print(f'{my_new_list} -->')
print(f'{max(my_new_list)}-{min(my_new_list)} -->')
result = max(my_new_list)-min(my_new_list)
print(round(result,2))

# num = int(input("Ведите число: ")) # = 5
# my_list = [for x in x range(num)]
# my_list = map()


