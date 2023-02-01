sum = lambda x: x+10
mult = lambda x: x**2
sum(mult(2))

sum1 = lambda x: x+22
mult2 = lambda x: x**3
sum1(mult2(2))

sum3 = lambda x: x+242
sum3(mult2(2))


f(g(x))

def h(f, g, x):
     return f(g(x))

h = lambda f, g, x: f(g(x))
h(sum, mult, 5)
h(lambda x: x+10, lambda x: x**2, 5)

def calc(op,a,b):
    print(op(a,b))
f = sum

def sum(x,y):
    return x+y

sum = lambda x, y: x+y
calc(sum,4,5)
calc(lambda x, y: x+y,4,5)


# К чему это всё?
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

f = open('f.txt', 'r')
data = f.read() + ' '
f.close()
numbers = []


while data != '':
   space_pos = data.index(' ')
   numbers.append(int(data[:space_pos]))
   data = data[space_pos+1:]
out = []
for e in numbers:
   if not e % 2:
    out.append((e,e **2))
print(out)


def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data))

--------------------------------------
# Создаем список:
li = [x for x in range(1,20)]
# получаем новый набор данных через функцию map
li=(map(lambda x: x+10, li))
# теперь преобразовываем в list
li = list(map(lambda x: x+10, li))


----------------------------------------
# будем заменять функцию select:
# получем набор данных и сразу разбиваем split список

data = input().split()
# список будем преобразовывать в функцию map, а в кач-ве аргумента 
# будем передавать ф-цию int
data = map(int,input().split())
# получаем, что лист из строк переводим в лист из чисел, а чтобы получить набор
# данных приводим к list
data = list(map(int(input().split())))
print(data)
# можем не преобразовывать в list, а пробежаться по нашим объектам

data = map(int,input().split()) 
for e in data:
    print(e)
--------------------------------------------------
# ручками создаем список
data = [x for x in range(10)]
# делаем выбор из четных элементов
res = filter(lambda x: x%2 == 0, data)
# преобразовываем к списку
res = list(filter(lambda x: not x%2, data))
print(res)

my_list = [2,3,5,9,3]
count = 0
for i in range(1,len(my_list),2):
    count+= my_list[i]
print(count)

сем 3 зад 1


my_list = [x for x in range(1,len(my_list))]
res = list(filter(lambda x: x%2 == 0, my_list))
res= list(map(lambda x: (x+x), res))
print(res)

---------------------------------------
# избавляемся от фунцкии where
data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)


# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
f(x) ⇒ x + 10
map(f, [ 1, 2, 3, 4, 5])
        ↓   ↓   ↓  ↓  ↓
     [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды


# Функция filter
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
f(x) ⇒ x - чётное
filter(f, [ 1, 2, 3, 4,5])
               ↓    ↓
              [ 2, 4 ]
# Нельзя пройтись дважды



# Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
zip ([1, 2, 3], [ 'о', 'д', 'т'], ['f','s','t'])
       ↓
[(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 114, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)



# Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
             ↓
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды