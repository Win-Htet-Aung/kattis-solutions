st = input()
maxi = 9699689
curSum = 0
cur = []
val = [1,2,6,30,210,2310,30030,510510]
for i in st.split():
	cur.append(int(i))

for i in range(8):
	curSum = curSum + (cur[i] * val[i])

print(maxi - curSum)