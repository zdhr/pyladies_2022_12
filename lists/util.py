import json


# Utilitka pro hezci výpis seznamů/slovníků
def pretty_print(value):
	print(json.dumps(value, indent=4, ensure_ascii=False))
