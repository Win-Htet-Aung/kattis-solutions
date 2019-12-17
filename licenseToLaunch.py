n = int(input())
st = input()
l = []
for i in st.split():
	l.append(int(i))

print(l.index(min(l)))