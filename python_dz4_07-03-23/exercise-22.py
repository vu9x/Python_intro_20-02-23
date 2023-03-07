import random

# Первое задание

first_list = [random.randint(0,10) for _ in range(10)]
second_list = [random.randint(0,10) for _ in range(10)]
matched_set = set()

print("Первый лист: ", first_list)
print("Второй лист: ", second_list)

for item in first_list:
    if item in second_list:
        matched_set.add(item)

print("Уникальные числа в обоих листах по возврастанию: ", sorted(matched_set, reverse=False))


# Второе задание
set_len_1 = int(input("Введите длину первого множества: "))
set_len_2 = int(input("Введите длину первого множества: "))

first_set = set()
second_set = set()

print("Введите значение первого множества")
while len(first_set) < set_len_1:
    x = int(input())
    first_set.add(x)

print("Введите значение второго множества")
while len(second_set) < set_len_2:
    x = int(input())
    second_set.add(x)


print(f"Длина: {set_len_1}, Первое множество {first_set}")
print(f"Длина: {set_len_2}, Второе множество {second_set}")
