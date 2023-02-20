# Найдите сумму цифр трехзначного числа.
number = int(input("Введите трехзначное число: "))
sum = 0

while number:
    sum += number % 10
    number /= 10

print(int(sum))

