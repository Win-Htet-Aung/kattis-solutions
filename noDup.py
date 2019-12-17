st = input()
wordLis = st.split()
wordSet = set(st.split())
if len(wordLis) - len(wordSet) == 0:
    print('yes')
else:
    print('no')