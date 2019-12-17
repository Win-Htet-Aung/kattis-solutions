def palin(s):
    if len(s) == 1:
        return True
    else:
        s1 = s[:int(len(s) / 2)]
        s2 = ''
        if len(s) % 2 == 0:
            s2 = s[int(len(s) / 2):]
        else:        
            s2 = s[int(len(s) / 2) + 1:]

        if s1[::-1] == s2:
            return True
        else:
            return False
