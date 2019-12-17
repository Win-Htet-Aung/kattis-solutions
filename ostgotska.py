st = input()
detect = 0
total = 0
for i in st.split():
    if 'ae' in i:
        detect+=1
    total+=1

if detect / total * 100 >= 40.0:
    print("dae ae ju traeligt va")
else:
    print('haer talar vi rikssvenska')