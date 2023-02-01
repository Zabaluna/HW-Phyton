# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_str = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
# new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
# print(new_str)  делали на занятии, но не учитывали знаки припенания

my_str = 'АБВ ылоажы фыыдлх абв, Зщышф вабвв ффлжв абВ!'
# my_str = my_str.lower()

result_list = []
find = 'абв'
symb = ['.',',','!','?',':']
for s in symb:
    my_str = my_str.replace(s, ' '+ s + ' ')
new_list = my_str.split()   
print(new_list)


for item in new_list:
    if not find.lower() in item.lower():
        result_list.append(item)
print(' '.join(result_list))

