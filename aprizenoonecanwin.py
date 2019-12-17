n, m = map(int, input().split())
prices = sorted(list(map(int, input().split())))
if len(prices) == 1:
	print(1)
else:
	items = [prices.pop(0), prices.pop(0)]
	while items[-1] + items[-2] <= m and prices:
		items.append(prices.pop(0))
	if items[-1] + items[-2] > m:
		print(len(items) - 1)
	else:
		print(len(items))
