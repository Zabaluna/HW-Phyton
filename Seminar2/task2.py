# 2. Для натурального n создать словарь индекс-значение,
#  состоящий из элементов последовательности 3n + 1.
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# num = int(input("Ведите число: "))
# d = {a: 3*a+1 for a in range(1, num+1)}
# print (d)


n = int(input('Print your N: '))
my_dict = {}
for i in range(1,n+1):
    my_dict[i] = 3*i+1
    print(my_dict)