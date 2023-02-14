import datetime
import json

date_format = '%Y.%m.%d'


# создание заметки
def create(title, body):
    all_notes = read_all()
    last_note_id = 0

    if len(all_notes) != 0:
        last_note_id = all_notes[-1]['id']

    note = {
        'id': last_note_id + 1,
        'created_on': datetime.datetime.now().strftime(date_format),
        'title': title,
        'body': body
    }

    all_notes.append(note)

    json_str = json.dumps(all_notes)
    with open('notes.json', 'w') as f:
        f.write(json_str)


# чтение всех заметок
def read_all():
    with open('notes.json', 'r') as f:
        file_content = f.read()
        all_notes = json.loads(file_content)

    return all_notes


# обновить заметку
def update(identifier, title, body):
    all_notes = read_all()

    for note in all_notes:
        if note['id'] == identifier:
            note['title'] = title
            note['body'] = body

    json_str = json.dumps(all_notes)
    with open('notes.json', 'w') as f:
        f.write(json_str)


# удалить заметку
def delete(identifier):
    all_notes = read_all()
    filtered = list(filter(lambda n: n['id'] != identifier, all_notes))

    json_str = json.dumps(filtered)
    with open('notes.json', 'w') as f:
        f.write(json_str)


command = input('enter command: ')

if command == 'add':
    title = input('title: ')
    body = input('body: ')
    create(title, body)

if command == 'readall':
    notes = read_all()
    print(notes)

if command == 'delete':
    id_to_delete = int(input("id: "))
    delete(id_to_delete)

if command == 'update':
    id_to_update = int(input("id: "))
    new_title = input("new title: ")
    new_body = input("new body: ")

    update(id_to_update, new_title, new_body)

if command == 'readone':
    id_to_print = int(input("id: "))
    all_notes = read_all()
    for note in all_notes:
        if note['id'] == id_to_print:
            print(note)

if command == 'readdate':
    date_from = datetime.datetime.strptime(input(f'date from {date_format}: '), date_format)
    date_to = datetime.datetime.strptime(input(f'date to {date_format}: '), date_format)

    all_notes = read_all()

    def date_in_range(note_to_check):
        date_string = note_to_check['created_on']
        date_obj = datetime.datetime.strptime(date_string, date_format)
        return date_from <= date_obj <= date_to

    filtered = list(filter(date_in_range, all_notes))

    print(filtered)