import view
import model
journal_test = { "Математика": { "Иванов": [ 2, 3 ], "Петров": [ 4, 5 ], "Сидоров": [ 5, 4 ] },
                 "Физика":     { "Иванов": [ 2, 3 ], "Петров": [ 4, 5 ], "Сидоров": [ 5, 5 ] },
                 "Русский":    { "Иванов": [ 2, 3 ], "Петров": [ 4, 5 ], "Сидоров": [ 5, 2 ] },
                 "Химия":      { "Иванов": [ 2, 3 ], "Петров": [ 4, 5 ], "Сидоров": [ 5, 3 ] } }

def start():
    path = 'database.txt'                                # /str/
    user_input = 0
    while user_input < 14:
        user_input = view.main_menu()       # вводится номер требуемого пункта меню /int/
        match user_input:
            # ниже перечень функционала для учителя
            case 1:
                # считать файл с БД (открыть файл)
                model.read_school_db(path)              # inp. /str/    ex. /list/
                school_db = model.get_school_db()       # inp.          ex. /list/
                view.db_success(school_db)              # inp. /list/   ex. /bool/                
                
            case 2:
                # открыть БД по определенному классу и конкретному предмету
                view.need_class(klass, subject)        # inp. /str, str/    ex. /dict - ?/

            case 3:
                # найти (вызвать) ученика
                search = view.search_request()          #               ex. /str/
                result = model.search_pupil(search)     # inp. /str/    ex. /dict - ?/
                view.show_contact_id(result)                 # inp. /str/    ex. /list - ?/

            # case 4:
                # поставить ученику оценку Решили не делать
                # search = view.search_request()          #               ex. /str/
                # result = model.search_pupil(search)     # inp. /str/    ex. /dict - ?/
                # model.mark_put(result, mark)            # inp. /dict, str/  ex.
                # view.mark_success()                     # inp.          ex. /str/ 'Оценка внесена в журнал'

            case 5:
                # добавить ученика
                new_pupil = view.create_pupil()         # inp.          ex. /dict -?/
                model.school_db.append(new_pupil)       # inp. /dict/   ex. /list/

            case 6:
                # изменить ученика
                search = view.search_request()          # inp.          ex. /str/
                result = model.search_pupil(search)     # inp. /str/    ex. /list/
                confirm = view.confirm_changes(result)  # inp. /list/   ex. /str/   y/n
                if 'n' not in confirm:
                    new_pupil = view.create_pupil()     # inp.          ex. /dict/          
                response = model.change_pupil(result,confirm,new_pupil) # inp. /list, str, list/    ex. /str/
                view.db_success(response)           # inp. /str/

            case 7:
                # удалить ученика
                search = view.search_request()          # inp.          ex. /str/
                result = model.search_pupil(search)     # inp. /str/    ex. /list/
                confirm = view.confirm_changes(result)  # inp. /list/   ex. /str/  y/n
                response = model.delete_contact(result,confirm) # inp. /list, str/ ex. /str/
                view.db_success(response)           # inp. /str/    ex. /str/ 'Ученик удален'

            case 8:
                # сохранить класс в файл с БД
                model.save_db(path)                     # inp. /str/    ex. updated file
                view.db_success()                     # inp.          ex. /str/ 'Файл сохранен'

    else:
        view.exit_program()                                    # inp.          ex. /str/ 'Завершение программы'