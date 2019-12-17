def is_prime(num):
	if num > 1:
		for i in range(2, int((num ** 0.5) + 1)):
			if num % i == 0:
				return i
				break
		# return True, 0
	else:
		return False, 2

t = int(input())
for i in range(t):
	st = input()
	n = int(st.split()[0])
	e = int(st.split()[1])
	p = is_prime(n)
	# print(p, n)
	q = n // p
	pq = (p-1) * (q-1)
	j = 1
	while (pq * j + 1) % e != 0:
		j += 1
	print((pq * j + 1) // e)