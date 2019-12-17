for i in range(int(input())):
	az = 'abcdefghijklmnopqrstuvwxyz'

	for j in map(lambda x: az.replace(x, ''), input().lower()):
		az = j

	for j in input().lower():
		az = az.replace(j, '')

	print('missing ' + az if az else 'pangram')










