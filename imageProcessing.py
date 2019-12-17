s = tuple(map(int, input().split()))
h, w, n, m = s

image = [list(map(int, input().split())) for i in range(h)]

kernel = [list(map(int, input().split())) for i in range(n)]
kernel.reverse()
for i in kernel:
	i.reverse()

ans = [[0] * (w-m+1) for i in range(h-n+1)]

for cc in range(w-m+1):
	for c in range(m):
		for rr in range(h-n+1):
			for r in range(n):
				ans[rr][cc] += image[rr+r][cc+c] * kernel[r][c]

for i in ans:
	for j in i:
		print(j, end = ' ')
	print()