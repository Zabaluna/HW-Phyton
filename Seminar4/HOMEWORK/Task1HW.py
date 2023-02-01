# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# from decimal import *
# from math import pi
# d = int(input('Print the given number precision '))
# getcontext().prec = d
# result = Decimal(pi)/Decimal(1)
# print(result)

# from math import pi

# d = int(input('Print the given number precision '))
# print('{round(pi, d)}')

import math
num = str(math.pi)
rounding_num = float(input('Задайте точность: '))
count = 0

while rounding_num < 1:
    rounding_num = rounding_num*10
    count +=1

print(num[:count+2])
