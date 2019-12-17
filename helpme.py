w = 'KQRBNP'
b = 'kqrbnp'
r = {15:'1',13:'2',11:'3',9:'4',7:'5',5:'6',3:'7',1:'8'}
c = {4:'a',8:'b',12:'c',16:'d',20:'e',24:'f',28:'g',32:'h'}
wp = {'K':[], 'Q':[], 'R':[], 'B':[], 'N':[], 'P':[]}
bp = {'k':[], 'q':[], 'r':[], 'b':[], 'n':[], 'p':[]}

for i in range(17):
    s = input()
    if i % 2 == 0:
        continue
    else:
        s = '..'+s
        for x in range(0, len(s), 4):
            if s[x] in w:
                wp[s[x]].append(r[i]+c[x])
            elif s[x] in b:
                bp[s[x]].append(r[i]+c[x])

#print(wp)
#print(bp)

wo = ''
bo = ''
for i, j in zip(w, b):
    if wp[i]:
        tempo = wp[i][:]
        tempo.sort()
        #print(tempo)
        for nadi in tempo:
            if i != 'P':
                wo = wo + i + nadi[::-1] + ','
            else:
                wo = wo + nadi[::-1] + ','
    if bp[j]:
        tempo = bp[j][:]
        #print(tempo)
        for nadi in tempo:
            if j != 'p':
                bo = bo + i + nadi[::-1] + ','
            else:
                bo = bo + nadi[::-1] + ','


print('White:', wo[:len(wo)-1])
print('Black:', bo[:len(bo)-1])
