# 1. Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.
#     *Пример:*
#     - 6782 -> 23
#     - 0,56 -> 11
#  Семинар2,задача1


# num = abs(float(input('Print your float number: ')))
# sum=0
# for i in str(num):
#     if i != '.' or i!=',':
#         sum += int(i)
# print(sum)


# num = abs(float(input('Print your float number: ')))
# sum = 0
# while num > 0:
#     sum += num % 10
#     num //= 10
# print(sum)

num = input('Print your number: ').replace('.','').replace(',','')
my_list = [int(i) for i in str(num)] #без map
my_list1 = list(map(int, str(num))) # с list и map
print(sum(my_list))
print(sum(my_list1))

