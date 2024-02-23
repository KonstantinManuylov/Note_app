from delete_note import notes_ids

def enter_title():
    return input("Введите заголовок: > ")


def enter_notes_body():
    return input("Введите текст заметки > ")


def create_id():
    try:
        ids = notes_ids()
        with open('notes.csv', 'r', encoding='utf-8') as file:
            return ids[-1] + 1
    except FileNotFoundError:
        return int(1)