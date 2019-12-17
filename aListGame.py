def is_prime(num):
	if num > 2:
		for i in range(2, int((num ** 0.5) + 1)):
			if num % i == 0:
				return False, i
				break
		return True, 0
	else:
		return False, 2

x = int(input())
k = 0
while x > 1:
	p, f = is_prime(x)
	if not p:
		k += 1
		x = x // f
	else:
		k += 1
		break
print(k)