import math as m
st = input()
x = int(st.split(' ')[0])
y = int(st.split(' ')[1])
pro = x * y

while m.ceil(float(pro) / x) == y:
	pro = pro - 1

print(pro + 1)