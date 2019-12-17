n = int(input())
st = input()
flis = []
for i in st.split(" "):
	flis.append(int(i))
slis = flis[:]
flis.sort()
ans = 0
if flis[n-1] == slis[0] or flis[0] == slis[n-1]:
	print(0)
else:
	for i in range(n):
		if flis[i] == slis[i]:
			ans = ans + 1
	print(ans)