from metodos_numericos import bisseccao
import math

def p2(x):
    return math.pow(x, 3)-87

def p(x):
    return math.pow(x, 5) - math.pow(x, 3) + (3*x) - 5


a = -8
b = +4

resultado = bisseccao(a, b, p)
print(resultado)

with open("resultado_atividade2.txt", "w") as f:
    f.write("x | erro r | erro x \n")
    for iteracao in resultado:
        f.write(str(iteracao)+"\n")


