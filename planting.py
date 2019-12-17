t = int(input())
st = input()
days = []
for i in st.split(' '):
	days.append(int(i))
days.sort()
for i in range(t):
	days[i] = days[i] - i
print(max(days)+t+1)