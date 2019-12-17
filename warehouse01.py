for i in range(int(input())):
    toy = []
    toy_count = []
    final_toy = []
    final_toy_count = []
    for i in range(int(input())):
        s = input().split()
        toy.append(s[0])
        toy_count.append(int(s[1]))
        
    for i in sorted(list(set(toy))):
        total = 0
        while i in toy:
            total += toy_count[toy.index(i)]
            toy_count.remove(toy_count[toy.index(i)])
            toy.remove(i)
        final_toy.append(i)
        final_toy_count.append(total)
    print(len(final_toy))
    final_list = []    
    for i in sorted(list(set(final_toy_count)))[::-1]:
        temp = []
        while i in final_toy_count:
            temp.append(final_toy[final_toy_count.index(i)])
            final_toy.remove(final_toy[final_toy_count.index(i)])
            final_toy_count.remove(i)
        final_list.append(i)
        final_list.append(temp)
        
        for i in sorted(final_list[1]):
            print(i, final_list[0])
        
        final_list = []
