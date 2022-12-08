# factorial 1 = 1
# factorial n = n * factorial(n-1)

def factorial(number):
	if number > 1:
		return number * factorial(number - 1)

	return 1

# fact 5 = 5 * fact(4)
# fact 5 = 5 * (4 * fact(3))
# fact 5 = 5 * (4 * (3 * fact(2)))
# fact 5 = 5 * (4 * (3 * (2 * fact(1))))
# fact 5 = 5 * (4 * (3 * (2 * (1))))
# fact 5 = 5 * (4 * (3 * (2)))
# fact 5 = 5 * (4 * (6))
# fact 5 = 5 * (24)
# fact 5 = 120

print(factorial(5))
