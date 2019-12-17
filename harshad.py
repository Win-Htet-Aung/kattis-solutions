def digSum(n):
	s = 0
	while n > 0:
		s = s + n % 10
		n = int(n / 10)
	return s

n = int(input())
while (n % digSum(n)) != 0:
	n += 1

print(n)
