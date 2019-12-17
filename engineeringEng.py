wordLis = []
ans = ''
st = input()
try:
	while st != '':
		for i in st.split(' '):
			if i.lower() not in wordLis:
				wordLis.append(i.lower())
				ans = ans + i + ' '
			else:
				ans = ans + '.' + ' '
		print(ans[:len(ans) - 1])
		ans = ''
		st = input()
except Exception:
	pass