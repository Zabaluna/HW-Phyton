# 5 Реализуйте алгоритм перемешивания списка.

import random

# my_list = [4,7,90,76,45,1234]
# print(my_list)
# random.shuffle(my_list)
# print(my_list)
# через shuffle

my_list1 = [4,7,90,76,45,1234]
print(str(my_list1))

for i in range(len(my_list1)-1, 0, -1):   
    j = random.randint(0, i)
    my_list1[i], my_list1[j] = my_list1[j], my_list1[i]
print(str(my_list1))   
# попыталась сделать по аналогии с задачей из семинара

