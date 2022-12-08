from util import pretty_print
from data import musicians


##
##	2. map() & filter()
##

# Jiný způsob transformace a filtrování seznamů.
# Oproti list comprehension může být pro některé čitelnější a lépe umožňuje
# znovupoužití kódu.


# Funkce které využijem pozděj. Obecně je lepší mít logiku ve funkcích, místo
# inline varianty. Je jedno jestli by mělo jít o lambdu, nebo list comprehension.
# Důvod je jednoduchý - DRY.

def is_female(musician):
	return musician['gender'] == 'female'

def is_in_band(musician):
	return musician['band'] is not None

def get_musician_info(musician):
	return f'{musician["name"]}: {musician["role"]}'


##
##	map()
##

# Funkce map(func, list) vytvoří ze seznam nový seznam, tak že na každý prvek z
# původního seznamu zavolá předanou funkci a její výsledek vloží do nového
# senzamu. Funkce vrací vlastní objekt, ten lze jednoduše převést na seznam
# pomocí list().

# V příkladu převedem seznam slovníků s informacemi o hudebnících na seznam
# stringů, které obsahují jejich jméno a roli ve skupině.
# Napřed klasicky:
musicians_info = []
for musician in musicians:
	musicians_info.append(get_musician_info(musician))

# A pomocí map() na jeden řádek
musicians_info2 = list(map(get_musician_info, musicians))

# Případně pomocí anonymní fuknce (lambdy), pokud jde o jednorázové použití.
musicians_info3 = list(map(
	lambda musician: f'{musician["name"]}: {musician["role"]}',
	musicians,
))

# pretty_print(musicians_info)
# pretty_print(musicians_info2)
# pretty_print(musicians_info3)


##
##	filter()
##

# Funkce filter(func, list) vytvoří ze seznam nový seznam. Do nového seznamu ale
# vloží pouze ty prvky z původního senzamu, pro které zadaná funkce vrátí True.
# Funkce vrací vlastní objekt, ten lze jednoduše převést na seznam pomocí list().

# V příkladu profiltrujeme seznam hudebníků, tak aby obsahoval pouze ženy.
# Napřed klasicky:
female_musicians = []
for musician in musicians:
	if is_female(musician):
		female_musicians.append(musician)

# A pomocí filter() na jednom řádku.
female_musicians2 = list(filter(is_female, musicians))

# Případně pomocí anonymní fuknce (lambdy), pokud jde o jednorázové použití.
female_musicians3 = list(filter(
	lambda musician: musician['gender'] == 'female',
	musicians,
))

# pretty_print(female_musicians)
# pretty_print(female_musicians2)
# pretty_print(female_musicians3)


##
##	Kombinace filter() a map()
##

# filter() a map() lze kombinovat. To je podle mně hlavní výhoda oproti list
# comprehension. Bohužel v pythonu se ten zápis stane hodně rychle velmi divoký,
# ale python není jedinný jazyk na světě :)

# Napřed je ale potřeba uvést na pravou míru jednu věc. Druhý parametr pro
# filter() a map() není seznam, ale cokoliv přes co lze iterovat - tzv. iterable.
# Pod toto spadají např. seznamy, stringy, výsledek z range() a taky výsledky
# z filter() a map().
# Když tedy chci použít výsledek z filter() jako parametr pro map(), tak jej
# nemusím převádět pomocí list().

result = []
for musician in musicians:
	if is_female(musician) and is_in_band(musician):
		result.append(get_musician_info(musician))

result2 = [
	get_musician_info(musician)
	for musician in musicians
	if is_female(musician) and is_in_band(musician)
]

result3 = list(map(
	get_musician_info,
	filter(is_female, filter(is_in_band, musicians))
))

# pretty_print(result)
# pretty_print(result2)
# pretty_print(result3)


# Je na vás jaký způsob si vyberete a který vám přijde nejčitelnější. Jenom je
# případně dobré zůstat konzistentní s již existujícím kódem.

# A komu přijde nejčitelnější toto...
# ... tak se uvidíme na lekci JavaScriptu pro pythnosty :)
# result4 = musicians
# 	.filter(is_female)
# 	.filter(is_in_band)
# 	.map(get_musician_info)
