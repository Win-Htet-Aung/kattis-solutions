pair = {'b':'$', 't':'|', 'j':'*'}
for i in range(int(input())):
    j = input()
    bag = []
    try:
        for item in j:
            if item in '$|*':
                bag.append(item)
            elif item in 'tjb':
                if bag[-1] == pair[item]:
                    bag.pop()
                else:
                    print('NO')
                    break
        else:
            if bag:
                print('NO')
            else:
                print('YES')
    except:
        print('NO')

