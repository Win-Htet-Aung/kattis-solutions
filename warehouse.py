for i in range(int(input())):
    warehouse = {}
    ship = int(input())
    
    for i in range(ship):
        shipment = input().split()
        toy = shipment[0]
        num = int(shipment[1])
        
        total = warehouse.setdefault(toy, 0)
        warehouse[toy] = total + num
    
    print(len(warehouse))
    for i in sorted(list(set(warehouse.values())))[::-1]:
        selected = [(x, y) for x, y in warehouse.items() if y == i]
        for j in sorted(selected):
            print(j[0], j[1])
