from logger import *
from edit_note import edit_note
from delete_note import delete_note

def interface():
    cmd = 0
    while cmd != '6':
        print("Выберите действие: \n"
              "1. Добавить новую заметку\n"
              "2. Вывести все заметки\n"
              "3. Поиск заметки\n"
              "4. Редактировать заметку\n"
              "5. Удалить заметку\n"
              "6. Выход\n")
        cmd = input("Введите действие: ")
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input("Введите действие: ")
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_all_notes()
            case '3':
                print(search_note())
            case '4':
                edit_note()
            case '5':
                delete_note()
            case '6':
                print('Всего доброго!')