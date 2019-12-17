st = input()
p = int(st.split()[0])
t = int(st.split()[1])
cases = p * t
case2D = []
for i in range(p):
    temp = []
    for j in range(t):
        if input()[1:].islower():
            temp.append(1)
        else:
            temp.append(0)
    case2D.append(sum(temp))
print(case2D.count(2))