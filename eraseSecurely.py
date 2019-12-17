n = int(input())
st = input()
fn = input()

def conBits(s):
	res = ''
	for i in s:
		if i == '1':
			res = res + '0'
		else:
			res = res + '1'
	return res


if n % 2 == 0:
	if fn == st:
		print('Deletion succeeded')
	else:
		print('Deletion failed')
else:
	if fn == conBits(st):
		print('Deletion succeeded')
	else:
		print('Deletion failed')