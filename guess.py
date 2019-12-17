guess = 500
low = 1
high = 1000
print(guess)
st = input()
while st != "correct":
	if st == 'lower':
		high = guess - 1
	else:
		low = guess + 1

	guess = int((low + high) / 2)
	print(guess)
	st = input()