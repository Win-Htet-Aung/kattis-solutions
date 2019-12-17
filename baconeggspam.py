n = int(input())
while n != 0:
	daily = {}
	for i in range(n):
		rec = input().split()
		name, food = rec[0], rec[1:]

		for f in food:
			daily.setdefault(f, []).append(name)

	for d in sorted(list(daily.keys())):
		print(d, ' '.join(sorted(daily[d])))

	n = int(input())