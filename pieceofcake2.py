n, h, v = map(int, input().split())
# print(4 * max(n - h, h) * max(n - v, v))
area = (n-h)*v if n-h > n-v else (n-v)*h if n-h < n-v else (n-h)**2
print(area * 4)