# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума)

import random

init_list = [random.randint(1, 10) for _ in range(10)]
print(init_list)

answer_list1 = []
answer_list2 = []
for i in range(len(init_list)):
    if init_list[i] >= 6 and init_list[i] <= 9:
        answer_list1.append(i)

answer_list2 = [i for i in range(len(init_list)) if init_list[i] >= 6 and init_list[i] <= 9]

print(answer_list1)
print(answer_list2)
        