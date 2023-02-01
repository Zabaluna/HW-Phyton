# 1. Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

import random

num = int(input("Ведите число: ")) #   = 5
a = []
for i in range(num):
    a.append(random.randint(-10,10) )
print(a)


# from itertools import count
# import random # имп. модуля

# num = int(input("Ведите число: "))

# a=[random.randint(-10,10) for i in range( num)]
# print (a)

#     #.randint - рандом целочисленного

#     #for i in range( num) - список