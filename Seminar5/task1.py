# 35. В файле находится N натуральных чисел, записанных через пробел.
#  Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#   Найдите это число.


# помпнять путь в переменных
# with open(r'D:\GB\PYTHON\Seminar5\New_file.txt', 'w') as f:
#     f.write('1 2 3 \n4 5 6 8 \n9 10 \n')
#     f.write('77 78\n79 80 81 \n')

# path = r'D:\GB\PYTHON\Seminar5\New_file.txt'
# data = open(path, 'r')
# num_row = []
# for line in data:
#     print(line)
#     num_row += list(map(int, line.split()))
# data.close()
# print(num_row)


# for i, elem in enumerate(num_row[:-1]):
#     if elem + 1 != num_row[i+1]:
#         print(elem + 1)
#         break

''''''
# from random import randint

# nums = [str(i) for i in range(22)]
# nums.pop(randint(1, 20))
# nums = ' '.join(nums)
# with open('num.txt', 'w', encoding='UTF-8') as data:
#     data.write(nums)

# with open('num.txt', 'r', encoding='UTF-8') as data:
#     numbers = list(map(int, data.readline().split()))
# print(numbers)
# for i in range(len(numbers) - 1):
#     if numbers[i] + 1 != numbers[i + 1]: 
#         print(numbers[i] + 1)
#         break
''''''''

data = '1 2 3 4 5 6 8 9'
# data=list(map(int, data.split()))
data=[int(x) for x in data.split()]
for i in range(len(data)-1):
    if not data[i]+1 == data[i +1]:
        print(data[i]+1)
  
# result = list(filter(lambda i: not data[i]+1 == data[i +1],range(len(data)-1)))

# for item in result:
#     print(data[item]+1)







# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
exit()
my_str = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
print(new_str)















