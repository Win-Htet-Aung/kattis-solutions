from collections import OrderedDict
s = input()
a = s.split(' ')[0]
b = s.split(' ')[1]

an = ''.join(OrderedDict.fromkeys(a))
bn = ''.join(OrderedDict.fromkeys(b))
af = 0
bf = 0

for i in an:
    if i in bn:
        af = a.index(i)
        bf = b.index(i)
        break

fd = '.' * af
bd = '.' * (len(a) - af - 1)
for i in range(len(b)):
    if i == bf:
        print(a)
    else:
        print(fd + b[i] + bd)

        
