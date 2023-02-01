# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
#  (1+1/n)^n
# и выведите на экран их сумму. 
#     *Пример:*
#     - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
n = int(input('Priny your N: '))
my_dict = {}
for i in range(1,n+1):
    my_dict[i] = (1+1/i)**i
    my_dict[i] = round(my_dict[i],2)
print(my_dict)

