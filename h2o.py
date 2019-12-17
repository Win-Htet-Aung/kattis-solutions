mo, nomo = tuple(input().split())
nomo = int(nomo)
p = noa = 0
modict = {}

for a in mo[::-1]:
    if a.isdigit():
        noa += (int(a) * 10 ** p)
        p += 1
    else:
        noa = 1 if noa == 0 else noa
        modict[a] = modict.get(a, 0) + noa * nomo
        noa = p = 0

p = noa = 0
dmo = input()
dmodict = {}
for a in dmo[::-1]:
    if a.isdigit():
        noa += (int(a) * 10 ** p)
        p += 1
    else:
        if a in modict:
            noa = 1 if noa == 0 else noa
            dmodict[a] = dmodict.get(a, 0) + noa
            noa = p = 0
        else:
            print(0)
            break
else:
    quo = []
    while dmodict:
        k, v = dmodict.popitem()
        quo.append(modict[k] // v)
    print(min(quo))