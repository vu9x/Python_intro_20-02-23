x = range(1, 1001)
y = range(1, 1001)

sum_xy = int(input("Подсказка 1 от Пети: сумма чисел x + y = "))
multiplier_xy = int(input("Подсказказ 2 от Пети: произведение x * y = "))

for i in x:
    for j in y:
        if i + j == sum_xy and i * j == multiplier_xy:
            print(f"Число x = {i}, число y = {j}")