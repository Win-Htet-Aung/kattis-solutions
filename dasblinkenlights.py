p, q, s = map(int, input().split())
print('yes' if set(range(p, s + 1, p)).intersection(set(range(q, s + 1, q))) else 'no')