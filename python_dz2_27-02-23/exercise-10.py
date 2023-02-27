monetki = [0, 0, 1, 1, 0, 1, 0]
reshka = 0
orel = 0

for x in monetki:
    if x == 0:
        reshka += 1
    else:
        orel += 1

if reshka < orel:
    print(f"Необходимо перевернуть минимально {reshka} решки")
else:
    print(f"Необходимо перевернуть минимально {orel} орла")