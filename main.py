import json
import datetime

def read_note():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    if not notes:
        print("Заметок нет")
    else:
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['date']})\n{note['body']}\n")
    return notes

def save_note():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def add_note():
    title = input("Введите название заметки: ")
    body = input("Введите тело заметки: ")
    note_id = len(notes) + 1
    date = datetime.datetime.now().isoformat()
    notes.append({"id": note_id, "title": title, "body": body, "date": date})
    save_note()
    print("Заметка успешно сохранена")

def edit_note():
    note_id = int(input("Введите id заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок: ")
            body = input("Введите новую заметку: ")
            note["title"] = title
            note["body"] = body
            note["date"] = datetime.datetime.now().isoformat()
            save_note()
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def delete_note():
    note_id = int(input("Введите id заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_note()
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным ID не найдена")

print("Редактор заметок в Python")
print("1. Создать заметку") 
print("2. Прочитать заметку") 
print("3. Редактировать заметку") 
print("4. Удалить заметку") 

notes = read_note()
command = int(input("Введите номер команды: "))

if command == 1:
    add_note()
elif command == 2:
    read_note
elif command == 3:
    edit_note()
elif command == 4:
    delete_note()
else:
    print("Неверная команда")
