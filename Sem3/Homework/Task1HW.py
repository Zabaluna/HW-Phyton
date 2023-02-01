# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2,3,5,9,3]
# count = 0
# for i in range(1,len(my_list),2):
#     count+= my_list[i]
# print(count)
# сем 3 зад 1
import math

my_list = [2,3,5,9,3]
my_list = [x for x in range(1,len(my_list))]
res = (list(filter(lambda x: x%2 == 0, my_list)))
res = ''.join(res)
res= sum(lambda x: (x+x), res)
print(res)


