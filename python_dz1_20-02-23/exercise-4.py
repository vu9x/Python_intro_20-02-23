# exercise 4
length = int(input("Введите кол-во долек шоколадки в длине: "))
width = int(input("Введите кол-во долек шоколадки в ширине: "))
number_of_pieces = int(input("Введите кол-во долек при одном разломе: "))

if number_of_pieces == width or number_of_pieces == (width * 2) or number_of_pieces == length:
    print("yes")
else:
    print("no")