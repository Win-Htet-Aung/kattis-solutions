import math as m
s = input()
while s != '0 0 0':
    r = float(s.split(' ')[0])
    tot = int(s.split(' ')[1])
    ins = int(s.split(' ')[2])
    print(m.pi * r**2, (ins/tot) * 4 * r**2)
    s = input()
