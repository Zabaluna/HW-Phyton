# 3. Напишите программу, которая определит позицию второго вхождения
#  строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(my_list)

string_find = "йцу"
count = 0
for i in range(len(my_list)):
    if string_find == my_list[i]:
        count+=1
        if count == 2:
            print(i)
            break
else:
    print(-1)


my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(my_list)

string_find = "йу"
count = -1
for i in range(len(my_list)):
    if string_find == my_list[i]:
        count+=1
        if count == 1:
            count = i
            print(i)
            break
else:
    print(count)


# my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# my_str = input('Введите строку')
# if my_str in my_list:
#     my_index = my_list.index(my_str)
#     if my_str in my_list[my_index + 1:]:
#         print(my_list[my_index + 1:].index(my_str))
#     else:
#         print(-1)
# else:
#     print(-1)

my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
my_str = input('Введите строку')

if my_list.count(my_str) > 1:
    my_index = my_list.index(my_str)
    print(my_list[my_index + 1:].index(my_str))
else:
    print(-1)


# my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# my_str = input('Введите строку')
# if my_str in my_list:
#     my_index = my_list.index(my_str)
#     if my_str in my_list[my_index + 1:]:
#         print(my_list[my_index + 1:].index(my_str))
#     else:
#         print(-1)
# else:
#     print(-1)

my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
my_str = input('Введите строку')

if my_list.count(my_str) > 1:
    first_index = my_list.index(my_str)
    print(my_list.index(my_str, first_index + 1))
else:
    print(-1)



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
