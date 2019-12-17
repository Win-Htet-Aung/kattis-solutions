import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

n = int(input())
if n == 1:
	print(0)
else:
	ans = 0
	for i in range(2, n + 1):
		ans += ncr(n, i)
	print(int(ans))