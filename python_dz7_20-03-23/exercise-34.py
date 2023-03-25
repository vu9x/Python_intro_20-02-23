vowels = "уеыаоэяию"
user_poem = "пара-ра-рам рам-пам-папам па-ра-па-да"
result = set()

phraze = lambda poem: poem.split()
use_phraze = phraze(user_poem)

for i in use_phraze:
    result.add(len(list(filter(lambda x: x in vowels, i))))
    
print("Парам пам-пам") if len(result) == 1 else print("Пам парам")
    

# def vowel_counter(phraze):
#     vowels = "уеыаоэяию"
#     counter = 0
#     for i in phraze:
#         if i in vowels:
#             counter += 1
#     return counter

# def phraze_spliter(phraze):
#     return phraze.split()

# poem = "пара-ра-рам рам-пам-папам па-ра-па-да"
# phraze_1 = phraze_spliter(poem)
# print(phraze_1)

# for i in phraze_1:
#     print(vowel_counter(i))
