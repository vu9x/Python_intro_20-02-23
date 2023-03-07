char_dict = {
    1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"],
    2: ["D", "G", "Д", "К", "Л", "М", "П", "У"],
    3: ["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"],
    4: ["F", "H", "V", "W", "Y", "Й", "Ы"],
    5: ["K", "Ж", "З", "Х", "Ц", "Ч"],
    8: ["J", "X", "Ш", "Э", "Ю"],
    10: ["Q", "Z", "Ф", "Щ", "Ъ"]
    }

counter = 0

user_word = input("Введите ваше слово: ").upper()

for char in user_word:
    for key in char_dict:
        if char in char_dict[key]:
            counter += key
            print(key, char, char_dict[key])

print(counter)