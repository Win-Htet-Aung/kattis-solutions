rec = []
try:
	while True:
		st = input()
		if st:
			rec.insert(0, st)
		else:
			ans = []
			l = len(rec[0])
			dl, star, dr = 0, 0, 0
			for i in rec:
				dl += star
				star = i.count('*')
				dr = l-dl-star
				ans.insert(0, dl*'.'+star*'*'+dr*'.')
			for i in ans:
				print(i)
			else:
				print()
			rec.clear()

except:
	ans = []
	l = len(rec[0])
	dl, star, dr = 0, 0, 0
	for i in rec:
		dl += star
		star = i.count('*')
		dr = l-dl-star
		ans.insert(0, dl*'.'+star*'*'+dr*'.')
	for i in ans:
		print(i)
	else:
		print()
