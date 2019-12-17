import random as r

prehash = int(input())
token = r.randint(0, 10**9-1)

prehash = (prehash * 31 + ord(i)) % 1000000007

nexthash = (prehash * 7 + token) % 1000000007
print(nexthash)