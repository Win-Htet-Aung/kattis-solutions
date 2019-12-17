n = input().split()
while float(n[0]) or int(n[1]):
	d = float(n[0])
	points = []
	sour = set()
	for i in range(int(n[1])):
		points.append(tuple(map(float, input().split())))
	for i in range(int(n[1]) - 1):
		for j in range(i + 1, int(n[1])):
			if d > (((points[i][0] - points[j][0]) ** 2) + ((points[i][1] - points[j][1]) ** 2)) ** 0.5:
				sour.add(i)
				sour.add(j)
	print('{} sour, {} sweet'.format(len(sour), int(n[1]) - len(sour)))

	n = input().split()