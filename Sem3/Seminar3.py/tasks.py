
import random

numbers = list(range(10))
print(numbers)
for i in range(len(numbers)):
    numbers.insert(random.randint(0, len(numbers) - 1), numbers.pop(i))
print('\n', numbers)

import random


def list_shuffle(_list: list):
    shuffled_list = []
    temp_list = _list

    for _ in range(len(_list)):
        position = random.randint(0, len(temp_list) - 1)
        shuffled_list.append(temp_list.pop(position))
    return shuffled_list


print(list_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

for i in range(len(numbers)):
    numbers.insert(random.randint(0, len(numbers) - 1), numbers.pop(i))
print('\n', numbers)



