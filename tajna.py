import math
msg = input()
x = len(msg)
r = 0
c = 0
segLis = []
if x > 3:
	for i in range(int(math.sqrt(x)) + 1, 0, -1):
		if x % i == 0:
			r = i
			break
	c = int(x / r)
	if r > c:
		r, c = c, r
	y = 0
	ans = ''
	if r > 1:
		for j in range(r - 1, x, r):
			segLis.append(msg[y:j + 1])
			y = j + 1
		for row in range(r):
			for col in range(c):
				ans = ans + segLis[col][row]
		print(ans)
	else:
		print(msg)
else:
	print(msg)