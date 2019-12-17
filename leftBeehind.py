st = 'x'
ansLis = []
while st != '0 0':
	st = input()
	x = int(st.split(" ")[0])
	y = int(st.split(" ")[1])
	if x + y == 13:
		ans = 'Never speak again.'
	elif x == y:
		ans = 'Undecided.'
	elif x > y:
		ans = 'To the convention.'
	elif x < y:
		ans = 'Left beehind.'
	ansLis.append(ans)
for i in ansLis[:len(ansLis) - 1]:
	print(i)