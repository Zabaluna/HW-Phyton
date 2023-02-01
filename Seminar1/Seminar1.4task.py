# 2. Напишите программу, которая будет принимать на вход дробь и показывать
#  первую цифру дробной части числа.
#   *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# num = input('enter number: ')
# if '.' in num:
#     index_num = num.find('.')+1
#     print(num[index_num])
# elif ',' in num:
#     index_num = num.find(',')+1
#     print(num[index_num])
# else:
#     print('no')

# num = input('Введите дробное число: ')
# if num.isdigit():
#     print('нет')
# else:
#     num = int(float(num)*10 % 10)
#     print(num)

# a = float(input('Введите дробное число: '))
# n = int(a*10 % 10)
# print(n)


# user_number = float(input('Enter your number: '))
# print(user_number, end=' -> ')
# if user_number % 1 == 0:
#     print('no')
# else:
#     print(int(user_number % 1 * 10))

# num = float(input('Введите дробное число: '))
# print(num)
# if num % 1 == 0:
#     print('нет')
# else:
#     num = int(num*10 % 10)
#     print(num)
