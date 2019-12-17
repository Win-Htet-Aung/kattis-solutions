from fractions import Fraction as f
n, d = map(int, input().split('/'))
fah = f(n, d)
x = f(5, 9)
y = (fah - 32) * x
print('{}/{}'.format(y.numerator, y.denominator))
