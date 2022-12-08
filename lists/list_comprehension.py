from util import pretty_print
from data import musicians


# Základní použití následujících příkladů je transformace/filtrování jednoho
# seznamu na jiný. Například pokud potřebujeme zdvojnásobit všechna čísla v
# seznamu, nebo zjednodušit seznam slovníků apod.


##
##	1. list comprehension
##	(česky intenzionální seznamy)
##

# Jedoduchý způsob jak zkopírovat seznam je pomocí for cyklu:
musicians_copy = []
for musician in musicians:
	musicians_copy.append(musician)

# Toto lze zapsat úsporněji pomocí list comprehension.
# - Do hranatých závorek...
# - Druhá část - "for musician in musicians" - je to stejné jako ve for cyklu
# - První část - "musician" před for je hodnota co se dá výsledného seznamu
musicians_copy2 = [musician for musician in musicians]

# pretty_print(musicians_copy)
# pretty_print(musicians_copy2)


# Hodnotu která se přidá do seznamu lze upravit.
# V tomto příkladu chceme seznam jmen, ne celé slovníky.
# Napřed klasicky:
musicians_names = []
for musician in musicians:
	musicians_names.append(musician['name'])

# Pomocí list comprehension:
musicians_names2 = [musician['name'] for musician in musicians]

# pretty_print(musicians_names)
# pretty_print(musicians_names2)

# Jiný příklad - seznam sudých čísel, čísla z range() před přidáním do nového
# seznamu vynásobíme dvěma:
even_numbers = [2 * n for n in range(5)]  # [0, 2, 4, 6, 8]


# Nemusíme kopírvat celý seznam, lze vybrat jen některé prvky z něj.
# Seznam jmen jen některých hudebníků, napřed klasicky:
female_musicians_names = []
for musician in musicians:
	if musician['gender'] == 'female':
		female_musicians_names.append(musician['name'])

# Pomocí list comprehension
# - na konec za iteraci přidáme klíčové slovo if a výraz, který vrací True/False
# - pokud tento výraz vrátí True, tak se prvek přidá do výsledného seznamu.
female_musicians_names2 = [musician['name'] for musician in musicians if musician['gender'] == 'female']

# Osobně bych to napsal takto, aby mně to nelezlo ven z obrazovky,
# ale nevím co na to PEP8:
#
# female_musicians_names2 = [
# 	musician['name']
# 	for musician in musicians
# 	if musician['gender'] == 'female'
# ]

# pretty_print(female_musicians_names)
# pretty_print(female_musicians_names2)
