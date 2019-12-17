n = 1
t = int(input())
x = int(input())
for i in range(t - 1):
	y = int(input())
	if y < x:
		n += 1
	x = y
print(n)
