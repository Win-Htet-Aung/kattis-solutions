for i in range(int(input())):
	n = int(input())
	pos = [j for j in range(n)]
	cards = [0 for j in range(n)]
	m = 1
	while pos:
		for k in range(m):
			pos.append(pos.pop(0))
		cards[pos.pop(0)] = str(m)
		m += 1
	print(' '.join(cards))
