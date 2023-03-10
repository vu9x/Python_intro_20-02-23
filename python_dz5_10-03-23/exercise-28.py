def summa(a, b):
    b -= 1
    a += 1
    if b != 0:
        return summa(a, b)
    return a

print(summa(2, 2))