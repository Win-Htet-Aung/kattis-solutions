s = input().split()
n = int(s[0])
v1 = int(s[1])
v2 = int(s[2])

q = int(n / v1)
r = n % v1

if r == 0:
        print(q, 0)
else:
        while q >= 0:
                if r % v2 == 0:
                        print(q, int(r / v2))
                        break
                else:
                        q -= 1
                        r = n - v1 * q
        else:
                print('Impossible')
