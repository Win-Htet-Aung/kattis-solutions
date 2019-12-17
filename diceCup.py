str = input()

n1 = int(str.split(" ")[0])
n2 = int(str.split(" ")[1])
if n1 > n2:
	n1, n2 = n2, n1

for i in range(n1 + 1, n2 + 2):
	print(i)