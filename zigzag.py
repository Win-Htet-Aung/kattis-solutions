def zigzagWords(t, l):
    t=t.replace(' ','')
    s = ''
    if l == 1:
        return t
    else:
        for i in range(l-1,-1,-1):
            # print(i)
            temp = ''
            k = (l-1)*2
            ind = 0
            while ind < len(t):
                ind = k
              
    return s    
                
print(zigzagWords('hospital',3))