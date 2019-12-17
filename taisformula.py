n = int(input())
s = input().split()
t1 = int(s[0])
v1 = float(s[1])
total = 0
for i in range(n - 1):
	s = input().split()
	t2 = int(s[0])
	v2 = float(s[1])
	total += (v2 + v1) / 2 * (t2 - t1)
	t1 = t2
	v1 = v2

# for i in range(n - 1):
# 	total += (V[i] + V[i + 1]) / 2 * (T[i + 1] - T[i])
print(total / 1000)
