t = int(input())
b16 = '0123456789ABCDEF'
b8 = '01234567'

def isValid(val):
    if '8' in val or '9' in val:
        return False
    else:
        return True

def toDec(val, curBase):
    res = 0
    digs = len(val)
    power = 0
    if curBase == 8:
        if isValid(val):
            for i in range(digs - 1,-1,-1):
                res = res + b8.index(val[i]) * (8 ** power)
                power += 1
    else:
        for i in range(digs - 1, -1, -1):
            res = res + b16.index(val[i]) * (16 ** power)
            power += 1
    return res

for i in range(t):
    st = input()
    n = int(st.split()[0])
    value = st.split()[1]
    print(n, toDec(value, 8), int(value), toDec(value, 16))
