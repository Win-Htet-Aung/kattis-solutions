st = input()
lim = int(st.split()[0])
eve = int(st.split()[-1])
ans = 0
cur = 0
for i in range(eve):
	st = input()
	x = st.split()[0]
	y = int(st.split()[-1])
	if x == 'enter' and y + cur <= lim:
		cur += y
	elif x == 'enter' and y + cur > lim:
		ans += 1
	else:
		cur -= y

print(ans)