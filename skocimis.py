st = input()
a = int(st.split(' ')[0])
b = int(st.split(' ')[1])
c = int(st.split(' ')[2])
d1 = abs(a - b)
d2 = abs(b - c)

if d2 > d1:
  d1, d2 = d2, d1
  a, b = b, c

count = 0

for i in range(d1 - 1):
  count = count + 1
 
print(count)