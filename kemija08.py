s = input()
i = 0
while i < len(s):
    if s[i] in 'aeiou':
        print(s[i], end = '')
        i += 2
    else:
        print(s[i], end = '')
    i += 1
