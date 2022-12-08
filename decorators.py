import time

# Funkce co obaluje jakoukoliv jinou funkci
def timer(function):
	def wrapper():
		t = time.monotonic()
		function()
		print(f"{function} took: {time.monotonic() - t} seconds")

	return wrapper

@timer
def foo():
	print('Ahoj')

@timer
def foo2():
	for _ in range(20000000):
		print("", end="")

foo()
foo2()
