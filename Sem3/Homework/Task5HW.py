# 5 Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# формула фибоначчи:
# Fn=F(n−1)+F(n−2)


def fibonacci(n):
    if n >= 0:
        fibonacci_list = [0, 1]
        for i in range(1, n):
            fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
        return fibonacci_list[-1]
    else:
        minus_fobonacci_list = [0, 1]
        for i in range(1, -n):
            minus_fobonacci_list.append(
                minus_fobonacci_list[-2] - minus_fobonacci_list[-1])
           
        return minus_fobonacci_list[-1]

k = int(input("Print yor k: "))
result = []
for i in range(-k, k+1):
    result.append(fibonacci(i))
print(result)
