from note_create import *
from logger import search_note
from delete_note import notes_ids, confirmation

def edit_note():
    ids = notes_ids()
    print(f"Возможные идентификаторы заметок: {ids}")
    select_to_edit = int(input("Выберите идентификатор заметки для редактирования > "))
    if select_to_edit in ids:
        if confirmation(select_to_edit, f"Желаете редактировать заметку {select_to_edit}? "
                                        f"Введите y для удаления > "):
            new_title = enter_title()
            new_body = enter_notes_body()
            with open("notes.csv", "r+") as file_input:
                lines = file_input.readlines()
                lines[select_to_edit - 1] = f"{select_to_edit};{new_title};{new_body};\n"
                with open("notes.csv", "w") as output:
                    for line in lines:
                        output.write(line)
            print(f"Заметкаи {select_to_edit} изменена.")