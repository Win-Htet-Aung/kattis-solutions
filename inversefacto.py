facto = int(input())
n = 2
while facto // n != 1:
	facto = facto // n
	n += 1

print(n)