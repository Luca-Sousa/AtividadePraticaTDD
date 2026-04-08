def calcular_pontos(valor, categoria, aniversario=False):
    if categoria == 'PREMIUM':
        pontos = valor * 2
    else:
        pontos = valor

    if aniversario:
        pontos += 500

    return pontos
