L = int(input())
D = int(input())
X = int(input())

# def sod(n):
# 	ans = 0
# 	while int(n / 10) != 0:
# 		ans = ans + (n % 10)
# 		n = int(n / 10)

# 	return ans + n

def sod(n):
	ans = 0
	s = str(n)
	for i in s:
		ans = ans + int(i)
	return ans

lis = []

for i in range(L, D + 1):
	if sod(i) == X:
		lis.append(i)


print(lis[0])
print(lis[-1])

