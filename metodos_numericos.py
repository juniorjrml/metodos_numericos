import math
import time

# Função para executar como decorator e medir o tempo
def tempo_decorrido(acao):
    def wrapper(a, b, f):
        inicio = time.time()
        resultado = acao(a, b, f)
        fim = time.time()
        print("", end='\n')
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
                funcao=acao.__name__,
                tempo_total=str(fim - inicio), end='\n'))
        return resultado
    return wrapper


def big_o(n):
    return math.log(n, 10)


def abs_error(x, x_):
    return math.fabs(x-x_)


def fat(x):
    return math.factorial(x)


def p_taylor_expandida(x):
    def parcela(n):
        return math.pow(x, n) / fat(n)


    p = 0
    for parcelai in range(6):
        p += parcela(parcelai)
    return p


def p_taylor_horner(x):
    def produto(n):
        return (1/n) * x

    acumulado = 1 + produto(5)  # Inicializando o valor
    for i in range(4, 0, -1):  # De 4 a 1 (inclusive)
        acumulado = 1 + (produto(i) * acumulado)

    return acumulado


def exponecial(x):
    return math.exp(x)


def ponto_medio(a, b):
    return (a+b)/2


def existe_zero(a, b, f):
    if (f(a)*f(b)) < 0:
        return True
    else:
        return False

@tempo_decorrido
def bisseccao(a, b, f, parada=1):
    valores_proximos = []
    erros_r = []
    erros_x = []

    while parada > 1e-20:
        x = ponto_medio(a, b)
        if f(x) != 0:
            valores_proximos.append(x)
            erros_r.append(abs(f(x)))
            try:
                erros_x.append(abs_error(
                    valores_proximos[-1],
                    valores_proximos[-2]))

            except IndexError:
                erros_x.append(abs(valores_proximos[-1]))

            if existe_zero(a, x, f):
                b = x
            else:
                a = x

        else:
            resultado = []
            valores_proximos.append(x)
            erros_x.append(0)
            erros_r.append(0)
            for elemento in enumerate(valores_proximos):
                resultado.append([
                    elemento[1],
                    erros_r[elemento[0]],
                    erros_x[elemento[0]]
                ])
            resultado.append(len(valores_proximos))
            return resultado
        parada = erros_x[-1]  # Ultimo erro

    print("Erro ao encontrar")
    return len(valores_proximos)