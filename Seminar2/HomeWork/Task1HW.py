# 1. Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.
#     *Пример:*
#     - 6782 -> 23
#     - 0,56 -> 11

# num = abs(float(input('Print your float number: ')))
# # if num < 0:
# #     num *= -1
# while num % 1 != 0:
#     num = round(num*10, 10)
# print(num)

# sum = 0
# while num > 0:
#     sum += num % 10
#     num //= 10
# print(sum)

# первый вариант решения, как мы по с# решали, что-то похожее
# второй вариант это решение через строку

# num = abs(float(input('Print your float number: ')))
# sum=0
# for i in str(num):
#     if i != '.' or i!=',':
#         sum += int(i)
# print(sum)


num = input('Print your float number: ')
sum = sum(map(int, num.replace('.', '')))
print (sum)

