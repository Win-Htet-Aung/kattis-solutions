n = int(input())
plis = sorted([int(input()) for i in range(n)], reverse = True)
tot = sum(plis)

for i in range(2, len(plis), 3):
	tot -= plis[i]
print(tot)