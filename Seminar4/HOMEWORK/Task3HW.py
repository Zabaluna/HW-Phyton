# 3 Задайте последовательность чисел.
#  Напишите программу, которая выведет список
#  неповторяющихся элементов исходной последовательности.


# my_list = [2, 4, 7, 8, 34, 90, -34, 2, 7, -90, 7] #2 и 7
# print(my_list)
# my_new_list = []
# for i in range(0, len(my_list)):
#     for j in range(i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#            my_new_list.append(my_list[j])
# print(my_new_list) наоборот вывела только повторяющиеся значения

# my_list = [2, 4, 7, 8, 34, 90, -34, 2, 7, -90, 7]
# print(my_list)
# my_set = list(set(my_list))
# print(my_set) #убирает только задвоенные значения, тк множество хранит уникальные значения
# import random

list_originals = []
list_work = [1, 1, 0 , 2, 3, 4, 4, 5, 6 ]
for i in range(15):
    list_work.append(random.randint(0,7))

#не совсем конкретное задание ...
for i in list_work:
    if i not in list_originals:
        list_originals.append(i)
print(list_work)
#если нужно вывести только неповторяющиеся значения, т.е. без дубликатов        
print(list_originals)

#если нужно вывести только неповторяющиеся значения, т.е. исключить полностью те числа, что повторялись
for i in list_originals:
    if list_work.count(list_originals[i]) > 1:
        while list_work.count(list_originals[i]) > 0:
            list_work.pop(list_work.index(list_originals[i]))
print(list_work)

exit()
my_list = [2, 4, 7, 8, 34, 90, -34, 2, 7, -90, 7] #2 и 7
print(my_list)
my_new_list = [] 
for i in my_list:
    count=0
    for j in my_list:
        if i==j:
            count+=1
    if count == 1:
        my_new_list.append(i)
print(my_new_list)      

# import random

# def fill_number_list(n=10, min=1, max=10) -> list:
#     number_list = [random.randint(min, max)]
#     for i in range (1, n):
#         number_list.append(random.randint(min, max)) 
#     return number_list

# def main():
#     source_list = fill_number_list(10, 1, 10)
#     print(source_list)
#     unique_numbers = []
#     for i in source_list:
#         if source_list.count(i) == 1:
#             unique_numbers.append(i)
#     print(unique_numbers)

# if __name__ == '__main__':
#     main()

# def main():
#     user_array = []
#     result_array = []
#     user_array = list(map(int, input('Enter sequence of integer numbers. Use space bar to split. ').split()))

#     for element in user_array:
#         if user_array.count(element) == 1:
#             result_array.append(element)
#     print(f'Unique elements in array {user_array} are - ', end='')
#     print(result_array)


# if __name__ == "__main__":
#     main()


import random

list_originals = []
list_work = [1, 1, 0 , 2, 3, 4, 4, 5, 6 ]
# for i in range(15):
#     list_work.append(random.randint(0,7))

#не совсем конкретное задание ...
for i in list_work:
    if i not in list_originals:
        list_originals.append(i)
print(list_work)
#если нужно вывести только неповторяющиеся значения, т.е. без дубликатов        
print(list_originals)

#если нужно вывести только неповторяющиеся значения, т.е. исключить полностью те числа, что повторялись
for i in list_originals:
    if list_work.count(list_originals[i]) > 1:
        while list_work.count(list_originals[i]) > 0:
            list_work.pop(list_work.index(list_originals[i]))
print(list_work)

# import random

# def row_without_repeatitions(row: list) -> list:
#     sieve = {}
#     clean_row = []
#     for i in row:
#         if i in sieve:
#             sieve[i] += 1
#         else:
#             sieve.setdefault(i, 0)
#     for key, value in sieve.items():
#         if not value:
#             clean_row.append(key)

#     return clean_row


# if __name__ == '__main__':
#     row = [random.randint(1, 8) for _ in range(10)]
#     print(row)
#     print(row_without_repeatitions(row))
