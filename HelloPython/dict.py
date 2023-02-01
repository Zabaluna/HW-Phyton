# people_id = {}
# people_id[1]= {'name':'Stoun', 'age':'38', 'comment':'ok'}
# people_id[2]= {'name':'Mary', 'age':'18', 'comment':'not ok'}
# print(people_id)
# print(people_id[1]) # так же как и pop обращение по ключу
# print(people_id.get(1).get('name'))  #вытягиваем имя по 1му айдишнегу
# print(people_id.pop(1)) #вынули на печатьпервый словарик  {'name':'Stoun', 'age':'38', 'comment':'ok'}
# print(people_id) # после поп отсался только 2й словарик {2: {'name':'Mary', 'age':'18', 'comment':'not ok'}}
# my_dict ={'+':'one', '2':'two', 'com':'not ok'}
# my_dict['new_key'] = 'Plus new key'  #добавили новый ключ к словарю
# print(my_dict)

# my_dict1 ={'+':'one', '2':'two', '9':' ok'}
# my_dict2 ={'+':'1', '2':'ввввв', 'com':'not ok'}
# my_dict1.update(my_dict2)#  в первый словарь кладем значение по ключам второго, переписывает значения
# print(my_dict1)

# my_dict1 ={'+':'one', '2':'two', '9':' ok'}
# my_dict2 ={'+':'1', '2':'ввввв', 'com':'not ok'}
# keys = set()
# for i in my_dict1:
#     keys.add(i)
# print(keys) #{'2', '+', '9'}
# for i in my_dict2:
#     keys.add(i)
# print(keys) #{'2', '+', '9', 'com'}

# new_dict = {}
# for i in keys:
#     new_dict[i]=str(my_dict1.get(i, ''))+str(my_dict2.get(i, ''))
# print(my_dict1) # {'+': 'one', '2': 'two', '9': ' ok'}
# print(my_dict2) # {'+': '1', '2': 'ввввв', 'com': 'not ok'}
# print(new_dict) # {'2': 'twoввввв', '+': 'one1', '9': ' ok', 'com': 'not ok'}  

# storage ={'Ананас':3, 'Банан':2, 'Инжир':3}
# delivery ={'Ананас':5, 'Инжир':10, 'Лайм':7}
# check = {'Ананас':1, 'Инжир':8}
# keys = set()
# for i in storage:
#     keys.add(i)
# for i in delivery:
#     keys.add(i)
# new_dict = {}
# for i in keys:
#     new_dict[i]=storage.get(i, 0) + delivery.get(i, 0)
#     new_dict[i]=storage.get(i, 0) - check.get(i, 0)
# print(storage)# {'Ананас': 3, 'Банан': 2, 'Инжир': 3}
# print(delivery)# {'Ананас': 5, 'Банан': 10, 'Инжир': 7}
# print(new_dict)# {'Банан': 2, 'Ананас': 8, 'Лайм': 7, 'Инжир': 13}
# print(check)

# storage.update(delivery)
# print(storage)# {'Ананас': 5, 'Банан': 2, 'Инжир': 10, 'Лайм': 7}

# dict1 = {'Store': {'Guitar': 1, 'Piano': 5}}

# new_list = list(dict1)
# while True:
#     for key in range(len(dict1)):
#          print(key,dict1[key])

dict1 = {'Store': {'Guitar': 1, 'Piano': 5}}

print(dict1['return'].popitem()[0])


