t = int(input())
digits = '0123456789ACDEFHJKLMNPRTVWX'
confuse = 'BGIOQSUYZ'
replaceDict = {'B':'8', 'G':'C', 'I':'1', 'O':'0', 'Q':'0', 'S':'5', 'U':'V', 'Y':'V', 'Z':'2'}
formulaDigits = [2,4,5,7,8,10,11,13]

def b27tob10(b27Num):
    b10 = 0
    power = 0
    for i in range(7,-1,-1):
        b10 = b10 + digits.index(b27Num[i]) * (27 ** power)
        power += 1
    return b10

def calcChkDigit(b27Num):
    b27Sum = 0
    for i in range(8):
        b27Sum = b27Sum + (digits.index(b27Num[i]) * formulaDigits[i])
    return digits[b27Sum % 27]

for i in range(t):
    st = input()
    n = int(st.split()[0])
    txt = st.split()[1]
    for i in txt:
        if i in confuse:
            txt = txt.replace(i, replaceDict[i])

    chkDigit = txt[-1]
    b27 = txt[:-1]
    if calcChkDigit(b27) == chkDigit:
        print(n, b27tob10(b27))
    else:
        print(n, 'invalid')
    