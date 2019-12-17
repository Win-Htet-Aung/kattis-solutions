try:
	st = input()
	while st:
		indLis = []
		ans = ''
		for word in st.split(' '):
			if 'a' in word:
				indLis.append(word.index('a'))
			if 'e' in word:
				indLis.append(word.index('e'))
			if 'i' in word:
				indLis.append(word.index('i'))
			if 'o' in word:
				indLis.append(word.index('o'))
			if 'u' in word:
				indLis.append(word.index('u'))
			if 'y' in word:
				indLis.append(word.index('y'))
			indLis.sort()
			if indLis[0] == 0:
				ans = ans + word + 'yay '
			else:
				ans = ans + word[indLis[0]:] + word[:indLis[0]] + 'ay '
			indLis.clear()
		print(ans)
		st = input()

except Exception:
	pass