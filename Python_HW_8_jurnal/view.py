def main_menu() -> int:  # +
    print('Главное меню.')
    menu_list = [' Открыть файл с базой данных, вывести учеников',#show_contacts
                 ' Уточнить, для какого класса нужен журнал учеников', #need_class
                 ' Открыть журнал по нужному нам предмету', #show_tasks
                 ' Найти ученика в журнале', #search_request, show_contact_id
                 ' Вызвать ученика к доске',
                 ' Поставить оценку ученику',
                 ' Добавить ученика в журнал', #create_pupil
                 ' Редактирование контактов ученика',#confirm_changes
                 ' Удаление ученика из журнала',#delete_contact()
                 ' Выход'] #exit_program

    for i in range( len(menu_list) - 1  ):
        print( f'\t{i + 1}. {menu_list[i]}' )
    print( f'\t{0}. {menu_list[-1]}' )

    user_input = int(input('Введи команду >: '))
    # TODO: сделать валидацию

    return user_input

find_class = ''
path = 'schoolbase.txt'

def need_class() -> int:
    while True:
        try:
            find_class = input('Введите нужный вам класс 7а или 7б: ')
            print(find_class)
            if find_class not in ['7a', '7b']:
                print(f'Введите 7a или 7b')
            elif find_class in ['7a', '7b']:
                path = find_class +'.txt'
                return path
             
        except ValueError:
            print('Таких классов в нашей школе нет')





def show_tasks():
    jurnal = { "Математика": { "Иванов": [ 2, 3 ], "Петров": [ 4, 5 ], "Сидоров": [ 5, 4 ] },
                 "Физика":     { "Иванов": [ 2, 3 ], "Петров": [ 4, 5 ], "Сидоров": [ 5, 5 ] },
                 "Русский":    { "Иванов": [ 2, 3 ], "Петров": [ 4, 5 ], "Сидоров": [ 5, 2 ] },
                 "Химия":      { "Иванов": [ 2, 3 ], "Петров": [ 4, 5 ], "Сидоров": [ 5, 3 ] } }
    

    tasks_list = list(jurnal)
    while True:
        for key in range(len(jurnal)):
            print(key+1,tasks_list[key])
        n = input(f'Выберете нужный вам предмет: ')
        if 1 < int(n) < len(tasks_list)+1:        
            return n
        print('Вы ввели не верный номер предмета')


def search_request():
    # jurnal  =  {"Предмет1": {{"Имя1", "Фамилия1"}: [2, 3], {"Имя1", "Фамилия1"}: [4, 5], {"Имя1", "Фамилия1"}: [5, 6]},
    #          "Предмет2": {{"Имя1", "Фамилия1"}: [5, 6], {"Имя1", "Фамилия1"}: [5, 6], {"Имя1", "Фамилия1"}: [5, 6]}}
    keys = ['lastname', 'firstname']
    search_pupil = {}
    while True:
        search_pupil[keys[0]]=input('Введите фамилию ученика')
        search_pupil[keys[1]]=input('Введите имя ученика')
        return search_pupil # титл почему то не работает


def show_contact_id (id, rec):
    print(f'\t{id + 1}', end='. ')
    for v in rec.values():
        print(f'{v}', end=' ')
    print()

   


def show_contacts(jurnal: list):  
    for i in range(len(jurnal)):
        user_id = i + 1
        print(f'\t{user_id}', end='. ')
        for v in jurnal[i].values():
            print(f'{v}', end=' ')
        print()




def exit_program():  
    print('Завершение программы.')
    n = int(input('Вы уверены что хотите выйти?\n1. Да\n2. Нет \n'))
    if n == 1:
        return 1
    else:
        print('Попробуйте вызвать "Завершение программы" еще раз...')


def create_pupil():
    print('Запись нового ученика в журнал:')
    print(f'Вы уверены что хотите записать нового ученика \n1 - Да\n2 - Нет\n')
    while True:
                your_number = int(input(' Введите 1 или 2: '))
                if your_number == 1:
                    print('Изменение контакта.')
                    new_pupil = dict()
                    new_pupil['lastname'] = input('\tВведите фамилию ученика >: ')
                    new_pupil['firstname'] = input('\tВведите имя ученика >: ')
                    return new_pupil
                elif your_number == 2:
                    print('\n Изменение отменено')
                    return 
                else: 
                    print('Вы ввели не верный номер: нужно 1 или 2')
                return 

def confirm_changes():
    print(f'Вы уверены что хотите изменить контакт ученика \n1 - Да\n2 - Нет\n')
    while True:
            your_number = int(input(' Введите 1 или 2: '))
            if your_number == 1:
                print('Изменение контакта.')
                id = int(input('\tВведите id ученика >: '))
                pupil['id'] = id
                pupil = {}
                keys = ['lastname', 'firstname']
                for key in keys:
                    if key == 'lastname':
                        if input(f'Изменить поле "Фамилия"??\n1 - Да\n2 - Нет\n') == '1':
                            pupil['lastname'] = input('\tВведите фамилию >: ')
                    if key == 'firstname':
                        if input(f'Изменить поле "Имя"??\n1 - Да\n2 - Нет\n') == '1':
                            pupil['firstname'] = input('\tВведите имя >: ')
                
                return pupil
            elif your_number == 2:
                print('\n Удаление отменено')
                return {} 
            else:
                print('Вы ввели не верный номер: нужно 1 или 2')
            return 
               
        
            

def delete_contact():
    print(f'Вы уверены что хотите удалить контакт?\n1 - Да\n2 - Нет\n') 
    while True:
            your_number = int(input(' Введите 1 или 2: '))
            if your_number == 1:
                print(' Будем удалять контакт.')
                pupil = {}
                keys = ['lastname', 'firstname']
                pupil[keys[0]]=input('Введите фамилию ученика')
                pupil[keys[1]]=input('Введите имя ученика')
                return pupil
            elif your_number == 2:
                print('\n Удаление отменено')
                return {} 
            else:
                print('Вы ввели не верный номер: нужно 1 или 2')
            return 


def db_success( message: str ):
    print("[+]", message)

def db_unsuccess( message: str ):
    print("[!]", message)

  
# main_menu()

# def open_file(file_name):
#     with open(file_name, encoding='UTF-8') as f:
#         clas = []
#         for i, line in enumerate(f):
#             [str, {'rus':[]}]
#             name, subjects = line.strip().split('.')
#             clas.append([name,{}])
#             for subject in subjects.split(';'):
#                 journ=subject.split(':')
#             #print(journ) 
#                 clas[i][1][journ[0]] = journ[1].split(',')
#         print(clas)
#     return clas

# def save_file(file_name, clas):
#     with open(file_name, 'w', encoding='UTF-8') as f:
#         for i in range(len(clas)):
#             s = clas[i][0] + '.'
#             subj = []
#             for k, v in clas[i][1].items():
#                 subj.append(f"{k}:{','.join(v)}")
#             s += ';'.join(subj)
#             f.write(f'{s}')