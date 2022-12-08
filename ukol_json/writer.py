age = int(input('Zadej svůj věk: '))

with open('age.txt', mode='w', encoding='utf-8') as file_:
    print(age, file=file_)
