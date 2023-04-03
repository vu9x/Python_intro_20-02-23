import view
import model

# if __name__ == '__main__':
#     print('Controller')

def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранен')
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
            case 5:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта: ')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Контакт {model.get_phone_book()[index].get("name")} успешно изменен')
            case 6:
                return
            case 7:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер контакта, кого хотите удалить: ')
                    view.show_message(f'Контакт {model.get_phone_book()[index].get("name")} успешно удален')
                    model.delete_contact(pb, index)
                    view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 8:
                name = view.find_contact()
                matched_contacts = model.find_contact(name)
                view.show_contacts(matched_contacts, f'Вы не открыли тел. книгу или контакт с именем {name} нет в телефонной книге')
