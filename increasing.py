def almostIncreasingSequence(sequence):
    c = 0; i = 0; k = sequence[0]; ki = -1
    while c < 2:
        if sequence[i] >= sequence[i + 1]:
            c += 1
            if i == 0 or k > sequence[i + 1]:
                sequence.pop(i)
            else:
                sequence.pop(i + 1)
            k = sequence[ki + 1]                
            i -= 1
            if c > 1:
                return False
        i += 1
        if i == len(sequence) - 1:
            return True

lis = [1,2,1,2]
print(almostIncreasingSequence(lis))