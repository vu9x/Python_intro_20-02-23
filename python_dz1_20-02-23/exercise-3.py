# 4 задание
ticket_number = int(input("Введите 6-ти значное число: "))

first_half = int(ticket_number / 1000)
second_half = ticket_number % 1000

sum1 = 0
sum2 = 0

while first_half:
    sum1 += int(first_half % 10)
    first_half /= 10

while second_half:
    sum2 += int(second_half % 10)
    second_half /= 10

print (f"first_half = {first_half}, second_half = {second_half}")
print (f"sum1 = {sum1}, sum2 = {sum2}")

if sum1 == sum2:
    print("yes")
else:
    print("no")
