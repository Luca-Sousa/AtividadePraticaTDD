MULTIPLICADORES = {
    'NORMAL': 1,
    'PREMIUM': 2,
}

LIMITE_PONTOS = 10000
BONUS_ANIVERSARIO = 500


def calcular_pontos(valor, categoria, aniversario=False):
    multiplicador = MULTIPLICADORES.get(categoria, 1)
    pontos = valor * multiplicador

    if aniversario:
        pontos += BONUS_ANIVERSARIO

    return min(pontos, LIMITE_PONTOS)
