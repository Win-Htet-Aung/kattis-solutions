n = int(input())
nameLis = []

for i in range(n):
	nameLis.append(input())

increLis = sorted(nameLis)
decreLis = sorted(nameLis, reverse = True)

if nameLis == increLis:
	print("INCREASING")

elif nameLis == decreLis:
	print("DECREASING")

else:
	print("NEITHER")