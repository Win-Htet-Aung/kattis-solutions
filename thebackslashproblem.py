sp = "!\"#$%&'()*[\\]"
lvl = int(input())
try:
	while lvl != -1:
		s = input()
		if lvl > 0:
			ans = ''
			for c in s:
				if c in sp:
					ans += '\\' * (2 * 2 ** (lvl - 1) - 1)
				ans += c
			print(ans)
		else:
			print(s)
		lvl = int(input())

except Exception:
	pass