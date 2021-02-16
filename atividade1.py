from metodos_numericos import p_taylor_horner, p_taylor_expandida, exponecial, abs_error

def apresentacao_resultados(x):
    print("Quando aplicado a forma expandida de Taylor:")
    resultado_expandida = p_taylor_expandida(x)
    print("x: {}, resultado: {}".format(x, resultado_expandida))

    print("Quando aplicado a forma de horner:")
    resultado_horner = p_taylor_horner(x)
    print("x: {}, resultado: {}".format(x, resultado_horner))

    print("Quando aplicado a exponencial:")
    resultado_exponencial = exponecial(x)
    print("x: {}, resultado: {}".format(x, resultado_exponencial))

    if resultado_expandida == resultado_horner:
        print("Os valores sao iguais")
    else:
        print("O valor absoluto da diferença entre eles e {}".format(abs_error(resultado_expandida, resultado_horner)))

    print("O erro absoluto na aproximacao polinomial de f pela forma expandida e {}".format(
        abs_error(resultado_exponencial, resultado_expandida)))

    print("O erro absoluto na aproximacao polinomial de f pela forma horner e {}".format(
        abs_error(resultado_exponencial, resultado_horner)))


valores = [0.7, 0.1]

for i in valores:
    apresentacao_resultados(i)
