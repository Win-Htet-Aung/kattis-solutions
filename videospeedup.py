n, p, k = tuple(map(int, input().split()))
ts = list(map(int, input().split()))

durs = [ts[0], k - ts[-1]]
for i in range(1, len(ts)):
	durs.insert(-1, ts[i] - ts[i - 1])

orgLen = 0
for i in range(n + 1):
	orgLen = orgLen + durs[i] * (100 + p * i) / 100

print(orgLen)
