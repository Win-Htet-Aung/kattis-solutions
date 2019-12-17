n = int(input())
s1 = sum(range(1, n + 1))
s2 = sum(range(2, n + 2))
if s1 % 2 == 0 and s2 % 2 == 0:
	print('Even')
elif (s1 % 2 == 0 and s2 % 2 == 1) or (s1 % 2 == 1 and s2 % 2 == 0):
	print('Either')
else:
	print('Odd')