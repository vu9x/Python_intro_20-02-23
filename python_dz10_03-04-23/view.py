import text_fields

def main_menu() -> int:
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split('\n')) - 1
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print(f'Введите ЧИСЛО от 1 до {length_menu}')

def new_contact() -> str: 
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return [name, phone, comment]

def update_contact() -> str:
    name = input('Введите имя (или Enter -оставить без изменений): ')
    phone = input('Введите телефон (или Enter -оставить без изменений): ')
    comment = input('Введите комментарий (или Enter -оставить без изменений): ')
    return [name, phone, comment]

def index() -> int:
    return int(input('Введите индекс контакта: ')) - 1

def find_by_name():
    return input('Введите поисковый запрос: ')