inp = input()
h = int(inp.split(' ')[0])
w = int(inp.split(' ')[1])
n = int(inp.split(' ')[2])
inp = input()
bricks = []
for i in inp.split(' '):
	bricks.append(int(i))
x = w
for i in range(n):
	x = x - bricks[i]
	if x == 0:
		h = h - 1
		x = w
		if h == 0:
			print('YES')
			break
	elif (x < 0) or (x > 0 and i == n - 1):
		print('NO')
		break