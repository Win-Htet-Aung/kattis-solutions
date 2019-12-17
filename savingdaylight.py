try:
	while True:
		a, b, c, d, e = input().split()
		d = d.split(':')
		e = e.split(':')
		t1 = int(d[0]) * 60 + int(d[1])
		t2 = int(e[0]) * 60 + int(e[1])
		t = t2 - t1
		h, m = t // 60, t % 60
		print(a, b, c, h, 'hours', m, 'minutes')
except Exception:
	pass

