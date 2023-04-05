import phone_book
import view



def start():
    pb = phone_book.PhoneBook('Python_intro_20-02-23\python_dz10_03-04-23\phonebook.txt')

    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                print(pb)
            case 2:
                pb.new_contact(*view.new_contact())
            case 3:
                print(pb.search(view.find_by_name()))
            case 4:
                print(pb)
                pb.update(view.index(), *view.update_contact())
            case 5:
                print(pb)
                pb.delete(view.index())
            case 6:
                pb.save()
            case 7:
                break

