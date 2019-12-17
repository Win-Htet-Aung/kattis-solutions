def is_prime(num):
	if num > 1:
		for i in range(2, int((num ** 0.5) + 1)):
			if num % i == 0:
				return False
				break
		return True
	else:
		return False

def sod(num):
	res = 0
	if num > 9:
		while int(num / 10) > 0:
			res = res + (num % 10) ** 2
			num = int(num / 10)
		res = res + num ** 2

	else:
		res = num ** 2

	return res

def is_happy(n):
	sodLis = []
	while sod(n) != 1:
		if sod(n) not in sodLis:
			sodLis.append(sod(n))
		else:
			return False
			break
		n = sod(n)

	return True

t = int(input())
for i in range(t):
	st = input()
	can = int(st.split(' ')[1])
	if is_prime(can) and is_happy(can):
		print(i + 1, can, 'YES')
	else:
		print(i + 1, can, 'NO')