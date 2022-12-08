import json


person = {
	'name': input('Jak se jmenuješ? '),
	'age': int(input('Zadej svůj věk: ')),
}

with open('person.json', mode='w', encoding='utf-8') as file_:
    print(json.dumps(person), file=file_)
