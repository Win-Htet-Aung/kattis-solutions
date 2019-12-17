t = int(input())
for i in range(t):
	s = input()
	len_s = len(s)
	rs = ''
	ind = 1
	while ind <= len_s:
		rs = s[:ind] * (len_s // ind + 1)
		if s in rs:
			print(ind)
			break
		ind += 1
