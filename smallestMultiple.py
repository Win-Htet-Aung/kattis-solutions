import math as ma

def is_prime(num):
	if num > 2:
		for i in range(2, int((num ** 0.5) + 1)):
			if num % i == 0:
				return False, i
				break
		return True, 0
	else:
		return False, 0

ans = 1
st = input()
try:
	while st:
		n1 = int(st.split()[0])
		n2 = int(st.split()[1])
		g = ma.gcd(n1, n2)
		for i in range(2, len(st.split())):
			g = ma.gcd(g, int(st.split()[i]))
		print(g)
		st = input()
except Exception:
	pass