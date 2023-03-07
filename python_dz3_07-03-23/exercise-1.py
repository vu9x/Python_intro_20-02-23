import random

my_list = [random.randint(0, 10) for _ in range(10)]
print(my_list)

number_x = int(input("Введите число: "))

counter = 0

for item in my_list:
    if item == number_x:
        counter +=1

print(f"Число {number_x} в листе появлялся {counter} раз")
