# Задачи:

# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
#     *Примеры:* 
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# if (a*a==b or b*b==a):
#     print ('yes')
# else:
#     print('no')

# num1 = int(input())
# num2 = int(input())
# if num1 ** 2 == num2 or num2 ** 2 == num1:
#     print('да')
# else:
#     print("нет")


first_user_number = int(input(' Enter first number: '))
second_user_number = int(input(' Enter second number: '))
print (f'{first_user_number}, {second_user_number} ->', end=' ')

if first_user_number == second_user_number**2 or second_user_number == first_user_number**2:
    print ('yes')
else:
    print ('no')

# user_number = float(input('Enter your number: '))

# if (user_number % 5 == 0 and user_number % 10 == 0 or user_number % 15 == 0) and user_number % 30 != 0:
#     print('Your number is nice! :)')
# else:
#     print('Try again.')

# user_number = int(input('Enter your number: '))

# if (user_number % 5 == 0 and user_number % 10 == 0 or user_number % 15 == 0) and user_number % 30 != 0:
#     print('Your number is nice!')
# else:
#     print('Try again')

# user_number % 5 == 0 and user_number % 10 == 0 and user_number % 30 != 0 or user_number % 15 == 0 and user_number % 30 != 0

