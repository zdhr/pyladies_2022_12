1)
Napište program `writer.py`:
- Program se uživatele zeptá na jeho věk.
- Potom výsledek uloží do souboru `age.txt`


2)
Napište druhý program `reader.py`:
- Program přečte obsah souboru `age.txt` jako číslo
- A poté vypíše text: "Ahoj, za rok ti bude <věk + 1>"


3)
Upravte program `writer.py`:
Nově se bude ptát na jméno a věk.
Data která uživatel zadal si bude pogram interně uchovávat ve slovníku. Věk bude jako číslo.
```
person = {
	"name": ...
	"age": ...
}
```
Výsledek potom uloží do souboru `person.json`


4)
Upravte program `reader.py`:
- Nově bude načítat data ze souboru `person.json`
- A bude vypisovat text: "Ahoj <jméno>, za rok ti bude <věk + 1>"
