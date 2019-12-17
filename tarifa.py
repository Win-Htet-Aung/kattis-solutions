n = int(input())
t = int(input())
used = 0
for i in range(t):
	used = used + int(input())
print((n * (t+1)) - used)