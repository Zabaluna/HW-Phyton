# 1. Дан список чисел. Создайте список, в который попадают числа,
#  описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


# list = [2, 5, 2, 3, 4, 6, 1, 7]

# def inc_list(list):
#     result = [list[0]]
#     count = 0
#     for i in range(1,len(list)):
#         if list[i] > result[count]:
#             result.append(list[i])
#             count +=1
#     return result

# print(inc_list(list))            


# num_list = [1, 5, 2, 3, 4, 6, 1, 7]  
# print(num_list, end=' => ')

# min_num = num_list[0]

# for i in range(len(num_list)):
#     order_list = []
#     order_list.append(num_list[i])
#     min_num = num_list[i] 
#     for j in range(i,len(num_list)-1):
#         if num_list[j] > min_num:
#             min_num = num_list[j]
#             order_list.append(num_list[j])
#     if len(order_list) > 1:
#         print(order_list, end=' ')

# num_list = [2, 5, 2, 3, 4, 6, 1, 7]
# # num_list = [4, 1, 5, 2, 3, 4, 6, 1, 7, 3, 4, 6, 5]
# print(num_list)
# new_list = []
# temp = []
# for i in range(len(num_list) - 1):
#     if num_list[i] < num_list[i + 1]:
#         if num_list[i] not in temp:
#             temp.append(num_list[i])
#         temp.append(num_list[i + 1])
#     elif temp: 
#         new_list.append(temp)
#         temp = []
# if temp: new_list.append(temp)
# print(new_list)



data = [1, 5, 2, 3, 4, 6, 1, 7]
result=[]

for i in range(len(data)-1):
    temp = []
    temp.append(data[i])
    cur_max = data[i]
    for j in range(i+1, len(data)):
        if data[j] > cur_max:
            temp.append(data[j])
            cur_max = data[j]
    result.append(temp)  
print(data)
print(result)          