with open('age.txt', encoding='utf-8') as file_:
    age = int(file_.read())

print(f'Za rok ti bude {age + 1}')
