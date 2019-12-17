no_of_teas = int(input())
tea_price = list(map(int, input().split()))
no_of_toppings = int(input())
topping_price = list(map(int, input().split()))

cost = []

for i in range(no_of_teas):
    for j in input().split()[1:]:
        cost.append(tea_price[i] + topping_price[int(j) - 1])

#print(cost)        
cost = min(cost)
#print(cost)
money = int(input())

cups = money // cost
if cups > 1:
    print(cups - 1)
else:
    print(0)
    
