N = int(input("Введите число N "))

total = 1
n_range = range(1, N)

for i in n_range:
    total *=2
    print(f"2^{i} = {total}")