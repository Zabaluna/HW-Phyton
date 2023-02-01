# 5 Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.


# Открываем 2 наших записанных файла txt, выводим на печать
with open('D:\GB\PYTHON\Seminar4\HOMEWORK\\new_equation_k.txt', 'r') as filek:
    second2 = filek.read()
with open('D:\GB\PYTHON\Seminar4\HOMEWORK\\new_equation2_k.txt', 'r') as filek:
    first1 = filek.read()

print(f"{first1} Первый многочлен ")
print(f"{second2} Второй многочлен")

# переводим наши многочлены обратно в словарь: ключ значение
def backdictinary(polinomilal: str) -> dict:
    polinomilal = polinomilal.replace('+', '').replace(' x',' 1*x').replace('*x ', '*x**1')
    polinomilal = polinomilal.split()[:-2] # берем срез, чтобы 0 и = отвалились
    dict_equation = {}
    # for i in range(len(polinomilal)):
    #    polinomilal[i] = polinomilal[i].split('*x**')
    for item in polinomilal:
        i = item.split('*x**')
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        else:
            dict_equation[0] = int(i[0])
    return dict_equation


#  выводим на печать первый и второй словарь, который получился из многочленов 
dict_equation1 = backdictinary(first1)
print(dict_equation1)

dict_equation2 = backdictinary(second2)
print(dict_equation2)

print(dict_equation1|dict_equation2)

# суммируем наши многочлены по ключам(если ключа нет,то берется ноль)
def addition(first_eq: dict, second_eq: dict):
    final_eq = {}
    final_eq.update(first_eq)
    final_eq.update(second_eq)
    for key in final_eq:
        final_eq[key] = first_eq.get(key, 0) + second_eq.get(key, 0)
    return final_eq    


final_eq = addition(backdictinary(first1), backdictinary(second2))
print(final_eq)

with open("D:\GB\PYTHON\Seminar4\HOMEWORK\\final_sum_polinoms.txt", "w", encoding='UTF-8') as filek:
        filek.write(str(final_eq))