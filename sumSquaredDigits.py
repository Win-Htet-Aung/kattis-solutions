t = int(input())
d1 = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
	  '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
numbers = '0123456789abcdef'

def dec_to_any_base(n, b):
	res = ''
	while n:
		res = numbers[n % b] + res
		n = n // b
	return res

for i in range(t):
	s = input().split()
	b = int(s[1])
	n = int(s[2])
	ans = 0
	for j in dec_to_any_base(n, b):
		ans += d1[j] ** 2

	print('{} {}'.format(i + 1, ans))
