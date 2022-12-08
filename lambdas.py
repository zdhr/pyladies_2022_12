# Obyčejný zápis funkce
def add(a, b):
	return a + b

# Do proměnných lze ukládat reference (odkazy) na funkce.
add(2, 5) # vrátí 7
secti = add # secti teď odkazuje na funkci add.
secti(2, 5) # opět vrátí 7

# Když sme líní psát, nebo potřebujeme jednorázově zadefinovat jednoduchou
# funkci na místě, kde nelze použít klasická definice:
# - Klíčové slovo "lambda"
# - seznam parametrů oddělený čárkama
# - dvojtečka
# - To co se má vrátit (bez klíčového slova "return")
# - To celé uložíme do proměnné
multiply = lambda a, b: a * b

# Lze volat jako klasickou funkci
multiply(2, 3) # vrátí 6
vynasob = multiply # totéž jako výše, nebo jako u slovníků/seznamů
vynasob(2, 3) # opět vrátí 6

# Lambdám se někdy říká anonymní funkce, to protože jejich nejčastěší je použití
# je jako parametr jiné funkce, kdy ani nedostanou jméno.
# Toto slouží jako ukázka toho jak vypadá, co přesně dělá filter je vedle
# v části o seznamech.
result = list(filter(lambda char: char.isupper(), 'aHoJ'))

# Nebo přehledněj rozepsané na řádky:
result2 = list(filter(
	lambda char: char.isupper(),
	'aHoJ',
))

# výsledek je ['H', 'J'] btw.
