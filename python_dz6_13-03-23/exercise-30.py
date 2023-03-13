# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

user_input = input("Введите через запятую: 1й элемент, разность, количество элементов: ").split(", ")

answer_list2 = [(int(user_input[0]) + i * int(user_input[1])) for i in range(int(user_input[2]))]
print(answer_list2)

# user_int = [int(x) for x in user_input]

# answer_list = []
# for i in range(user_int[2]):
#     answer_list.append(user_int[0] + i * user_int[1])
# print(answer_list)