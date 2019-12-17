import math
n = int(input())
p = 0

while 2 ** p < n:
	p = p + 1

size = 2 ** p

while n != 0:
	if n >= size:
		n = n - size
	else:
		size = size / 2

print(2 ** p, p - int(math.log(size, 2)))