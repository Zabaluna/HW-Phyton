# 2. Напишите программу, которая принимает на вход число N и
#  выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input('Print your N: '))

fact = 1
for i in range(1,n+1):
    fact*=i
    print(fact, end =' ')

# Функция факториала из листа подсказки))    
n = int(input('Print your N: '))    
def fact(n):  # Обычная функция факториала
    pr=1
    a=[]
    for i in range(1,n+1):
        pr=pr*i
        a.append(pr)
    return a
print(fact(n))