from note_create import *
from delete_note import notes_ids

def enter_data():
    title = enter_title()
    body = enter_notes_body()
    note_id = create_id()
    with open('notes.csv', 'a', encoding='utf-8') as file:
        file.write(f'{int(note_id)};{title};{body};\n')


def print_all_notes():
    try:
        file = open('notes.csv', 'r', encoding='utf-8')
        print(file.read())
    except:
        print("Файла не существует. Созадйте новую заметку.")


def search_note():
    ids = notes_ids();
    print(f"Возможные идентификаторы заметок: {ids}")
    searched = int(input("Введите идентификатор заметки: > ")) - 1
    try:
        with open('notes.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if searched not in len(lines) - 1:
                return f"Нет заметки с идентификатором {searched}."
            return lines[searched]
    except FileNotFoundError:
        return print("Файла не существует. Созадйте новую заметку.")
