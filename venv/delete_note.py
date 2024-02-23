def notes_ids():
    result: list[int] = []
    with open('notes.csv', 'r', encoding='utf-8') as file:
        data = file.read().strip().split(';')
        for item in data:
            item = item.strip()
            if item.isdigit():
                result.append(int(item))
    return result


def confirmation(selection: chr, msg: str) -> bool:
    confirm = input(msg).lower()
    if confirm == "y":
        return True
    return False


def delete_note():
    ids = notes_ids()
    print(f"Возможные идентификаторы заметок: {ids}")
    select_to_delete = int(input("Выберите идентификатор заметки для его удаления > "))
    if select_to_delete in ids:
        if confirmation(select_to_delete, f"Желаете удалить заметку {select_to_delete}? "
                                          f"Введите y для удаления > "):
            with open("notes.csv", "r") as file_input:
                lines = file_input.readlines()
                searched_line = lines[select_to_delete - 1]
                with open("notes.csv", "w") as output:
                    for line in lines:
                        if line != searched_line:
                            output.write(line)
        print(f"Удаление заметки {select_to_delete} завершено.")
