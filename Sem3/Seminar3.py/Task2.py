# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

import os
os.system("clear")

list1 = ["2", "43", "5", "331", "91", "35", "79", "53"]
x = input("Введите число: ")

for i in list1:
    if x == i:
        print(f"число {i} присутствует в списке")
        break
else:
    print("заданное число отсутствует в списке")


def check(stringlist: list, n: str) -> bool:
    for i in stringlist:
        if n == i:
            return True
    return False

my_list = ["2", "3", "3425", "0", "-1"]
x = input("Введите искомое число: ")
if check(my_list, x):
    print("Число есть в последовательности", my_list)
else:
    print("Числа нет в последовательности", my_list)
