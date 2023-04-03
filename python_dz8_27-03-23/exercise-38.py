# 1. Открыть файл тел. книги
# 2. Сохранить файл тел. книги
# 3. Показать все контакты
# 4. Найти контакты
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# Имя
# Номер
# Коммент

import os, json


# basepath = os.getcwd()
os.chdir('python_dz8_27-03-23')

def menu():
    append_file_dir()

    if open_read_dir():
            phonebook = open_read_dir()
    else: phonebook = {}

    while True:
        anc = int(input('Введите запрос:\n'
                        '1. Открыть файл тел. книги\n'
                        '2. Сохранить файл тел. книги\n'
                        '3. Показать все контакты\n'
                        '4. Найти контакты\n'
                        '5. Добавить контакт\n'
                        '6. Изменить контакт\n'
                        '7. Удалить контакт\n'
                        '8. Выход\n'))

        if anc ==1:
            book = open_read_dir()
            print(book)
        elif anc == 2:
            save_dir(phonebook)
        elif anc == 3:
            for contact, telephone in phonebook.items():
                print(f'{contact}: {telephone}')
        elif anc == 4:
            name = input("Кого хотите найти? ")
            if phonebook.get(name):
                print(f"Телефон {name}: {phonebook[name]}")
            else: print("Такого контакта не существует")
        elif anc == 5:
            name = input("Введите имя: ")
            phone = input("Введите телефон: ")
            phonebook[name] = phone
            save_dir(phonebook)
        elif anc == 6:
            name = input("Кого хотите изменить: ")
            phone_upd = input("Введите обновленный телефон: ")
            if phonebook.get(name):
                phonebook[name] = phone_upd
                print(f"Вы успешно обновили контакт {name}/ Не забудьте сохранить\нажать на 2")
            else: print("Такого контакта не существует")
        elif anc == 7:
            name = input("Кого хотите удалить: ")
            if phonebook.get(name):
                print(f"Телефон {name} удален")
                del phonebook[name]
                save_dir(phonebook)
            else: print("Такого контакта не существует")
        elif anc == 8:
            print('End')
            break
        else:
            print('Введите ещё раз')


def open_read_dir():
    with open('phonebook.txt', 'r', encoding='utf-8')  as f:
        return json.loads(f.read())

def append_file_dir():
    with open('phonebook.txt', 'a')  as f:
        f.close()

def save_dir(dict_phnbk):
    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(dict_phnbk))

menu()

