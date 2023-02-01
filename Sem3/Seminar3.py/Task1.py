# 1 Реализуйте алгоритм задания случайных чисел без использования
#  встроенного генератора псевдослучайных чисел.

import time
current_time = time.time()
print(current_time)
rand_num = int(1000 * current_time)
print(rand_num)
print(rand_num % 100)
print(str(rand_num)[-5:])