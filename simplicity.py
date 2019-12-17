letters = {}
for i in input():
	n = letters.setdefault(i, 0)
	letters[i] = n + 1

simplicity = len(letters)
counts = sorted(list(letters.values()))
if simplicity > 2:
	ans = 0
	for i in range(simplicity - 2):
		ans += counts[i]
	print(ans)
else:
	print(0)
