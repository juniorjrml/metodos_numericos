from metodos_numericos import bisseccao
import math


def p(x):
    return math.pow(x, 5) - math.pow(x, 3) + (3*x) - 5

a = -4
b = +4

a = bisseccao(a, b, p)
print(a)
print("x | erro r | erro x")
for i in a:
    print(i)