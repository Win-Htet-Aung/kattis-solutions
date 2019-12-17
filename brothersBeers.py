def brothersInTheBar(glasses):
    i = 0
    count = 0
    while i < len(glasses) - 2 and len(glasses) > 2:
        temp = glasses[i:i+3]
        print(temp, i)
        if sum(temp) == temp[0] * 3:
            for j in range(3):
                del(glasses[i])
            count+=1
            i = 0
            print(glasses, i)
        else:
            i+=1
    return count

print(brothersInTheBar([1, 1, 2, 3, 3, 3, 2, 2, 1, 1]))

