print('hello world')

#типы данных и переменные
#int,float,bool,str,list,None 
value = None
a = 123
b = 1.23
print(type(b))
print(type(a))
value = 1234
print(type(value))

s = 'Hello world'
print(s)

# s = 'Hello \nworld' # вывод с новой строки \n
print(s) # вывод строки
print(a,'-',b,'-',s)
print('{} - {} - {}'.format(a,b,s))
print(f'{a} - {b} - {s}')

Ввод и вывод данных
print, input
print('Введите a');
a = float(input())
print ('Введите b');
b = int(input())
print(a, ' + ', b, ' = ', a+b)

# Арифметические операции
a = 10
b = 3
# c = a/b # деление в веществ числах
# print(c)
# c = a//b # деление только целая часть
# print(c)
# c = a%b  # остаток от деления
# print(c)
# # c = round(a*b, 3) # округление до 3х знаков, без откругления округляет в большую степень до целого
# print(c)
c = a**b # возведение в степень
print(c)

Логические операции
not, and, or - не путать с &,|, ^
is, is not, not in
gen

f = [1,2,3,4]
print(f)
print(2 in f) № наличие 2 в списке
print(5 in f)
print(not 2 in f) # отрицание наличия 2 в списке
is_odd = f[0] % 2 == 0
print(is_odd)
is_odd = not f[0] % 2
print(is_odd)

Управляющие конструкицц
if, if - else
a = int(input('Введите a '))
b = int(input('Введите b '))
if a > b:
    print(a)
else:
    print(b)

username = input('Введите имя ')
if username == 'Маша':
    print('Ура, Маша')
elif username == 'Марина':
    print('Отлично. Марина')
elif username == 'Коля':
    print('Колян, привет')
else:
    print('Добрый день, ', username)

Цикл while

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original//= 10  # original = original // 10
    print(original)
    print(inverted)
else:
    print(' Пожалуй хватит')
print(inverted)
    
Управляющие конструкции for

for i in 1,2,3,4,5:
    print(3**i) # умножаем каждое i на 3

list = [1,2,5,7]
for i in list:
    print (i)

r = range(10)
for i in r:
    print(i)

r = range (4,10, 2) # в дипазоне делаем шаг в 2
for i in r:
    print(i)

Работа со строками
text = 'съешь еще этих мягких французких булок'
print(len(text)) #38 длина текста
print('еще' in text) # ищет такие же символы в тексте
print(text.isdigit()) # проверка, являются ли элементы числами
print(text.islower()) # проверка на нижний регистр 
print(text.replace('еще', 'ЕЩЕ')) # замена в тексте

print(text[0]) # поиск по номеру элемента
print(text[3])
print(text[len(text)-1]) # поиск последнего элемента буквы в тексте
print(text[len(text)-2]) # предпоследний элемент
print(text[-5]) # ищет элемент буквы с конца.используем минус
print(text[:]) # выводит все элеементы от первого до послнеднего
print(text[2:-7])
print(text[len(text)-2:]) # выводит от предпоследнего до последнего #ок
print(text[0:len(text):6]) #сеикаио
print(text[::6]) #сеикаио
print(text[0:len(text):2]) # убирает символ из текста
text= text[2:9] + text[-5]
print(text)

Списки: введение
list=list
numbers = [1,2,3,4,5]
print(numbers)
ran = range(1,6)
print(type(ran))
numbers = list(ran) # приведение типа лист к типу рандж
print(type(numbers))

print(numbers)
numbers[0] = 7 #заменяем элеемнт значением своим
print(f'{len(numbers)} len') # количество элеемнтов в списке
print(numbers)
for i in numbers:
    i*=2  # умножение элемента
    print(i)        #[2,4,6,8,10]
print(numbers)    

Добавление и удаление элементов в списках
colors = ['red', 'green', 'blue']
for e in colors:
    print(e)  # red green blue

for e in colors:
    print(e*2) # redred greengreen bleublue

colors.append('gray') #добавление в конце
print(colors)
print(colors==['red', 'green', 'blue','gray']) #True

colors.remove('red') #del colors[0] # удаление элемента
print(colors)

Функции
def f(x):
    if x==1:
        return 'Целое'
    elif x ==2.3:
        return 23
    else:
        return

arg = 7
print(f(arg))
print(type(f(arg)))
ррр