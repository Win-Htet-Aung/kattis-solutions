from math import log, floor, pi
def noOfDigits(n):
	return floor(((n+0.5) * log(n) - n + 0.5*log(2*pi))/log(10)) + 1

try:
	num = input()
	while True:
		if int(num) == 0 or int(num) == 1:
			print(1)
		else:
			print(noOfDigits(int(num)))
		num = input()
except Exception:
	pass