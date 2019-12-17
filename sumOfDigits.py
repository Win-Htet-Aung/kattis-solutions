def sod(n):
    res = 0
    while n > 0:
        res = res + n % 10
        n = int(n / 10)
    return res

def secretNumber(numberLength, sumOfDigits, k):
    sele = []
    for i in range(10**(numberLength - 1),10**numberLength-1,1):
        if sod(i) == sumOfDigits:
            sele.append(i)
    

#secretNumber(3,4,7)
print(sod(int(input())))
