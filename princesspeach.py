n, y = tuple(map(int, input().split()))
found = set([int(input()) for x in range(y)])
for i in range(n):
    if i not in found:
        print(i)

print('Mario got {} of the dangerous obstacles.'.format(len(found)))