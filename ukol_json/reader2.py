import json


with open('person.json', encoding='utf-8') as file_:
    # V podstatě ekvivalent načtení čísla z druhého kroku, ale pro JSON.
    # age = int(file_.read())
    person = json.loads(file_.read())

print(f'Ahoj {person["name"]}, za rok ti bude {person["age"] + 1}')
