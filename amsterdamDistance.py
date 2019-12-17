st = input()
a = int(st.split()[0])
b = int(st.split()[1])
r = float(st.split()[2])
cor = input()
x1 = int(cor.split()[0])
y1 = int(cor.split()[1])
x2 = int(cor.split()[2])
y2 = int(cor.split()[3])
if y1 > y2:
	y1, y2 = y2, y1

pi = 3.14159265358979323846
path1 = (r/(a*b)) * (y1*pi*(abs(x1-x2)) + (abs(y1-y2))*a)
path2 = (r/b) * (y1+y2)

if path1 < path2:
	print(path1)
else:
	print(path2)