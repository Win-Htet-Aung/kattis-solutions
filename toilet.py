up_down = input()
inip1 = inip2 = inip3 = up_down[0]
up_down = up_down[1:]

p1 = p2 = p3 = 0

for i in up_down:
	if i == 'U':
		if inip1 == 'D':
			p1 += 1
			inip1 = 'U'

		if inip2 == 'U':
			p2 += 1
			inip2 = 'D'
		else:
			p2 += 2

		if inip3 == 'D':
			p3 += 1
			inip3 = 'U'

	else:
		if inip1 == 'U':
			p1 += 2
		else:
			p1 += 1
			inip1 = 'U'

		if inip2 == 'U':
			p2 += 1
			inip2 = 'D'

		if inip3 == 'U':
			p3 += 1
			inip3 = 'D'

print(p1, p2, p3, sep = '\n')
