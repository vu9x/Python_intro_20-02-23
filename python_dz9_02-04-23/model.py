import os

phone_book = []
path = os.path.join(os.getcwd(),'Python_intro_20-02-23\phone_book.txt')


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()

    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name': fields[0],
                   'phone': fields[1],
                   'comment': fields[2]}
        phone_book.append(contact)

def get_phone_book():
    return phone_book

def add_contact(contact: dict):
    phone_book.append(contact)

def change_contact(contact: dict, index: int):
    phone_book.pop(index)
    phone_book.insert(index, contact)

def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join(list(contact.values())))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def delete_contact(contact: dict, index: int):
    phone_book.pop(index)
    save_file()

def find_contact(name: str):
    matched_contacts = []
    for contact in phone_book:
        if name in contact.get('name'):
            matched_contacts.append(contact)
    return matched_contacts