import unittest
from fidelidade import calcular_pontos

class TestFidelidade(unittest.TestCase):

    # =========================================================
    # UC01 — Pontuação Padrão
    # Regra: cada R$ 1,00 gasto = 1 ponto
    # =========================================================
    def test_ponto_padrao(self):
        # RED → GREEN: compra de R$ 100,00 deve retornar 100 pontos
        self.assertEqual(calcular_pontos(valor=100.0, categoria='NORMAL'), 100)

    # =========================================================
    # UC02 — Bônus de Categoria "Premium"
    # Regra: categoria PREMIUM = dobro de pontos (2 pts por real)
    # =========================================================
    def test_bonus_premium(self):
        # RED → GREEN: compra de R$ 100,00 com PREMIUM deve retornar 200 pontos
        self.assertEqual(calcular_pontos(valor=100.0, categoria='PREMIUM'), 200)

    # =========================================================
    # UC03 — Promoção de Aniversário
    # Regra: mês de aniversário = +500 pontos fixos sobre o total
    # =========================================================
    def test_bonus_aniversario(self):
        # RED → GREEN: R$ 100,00, NORMAL, aniversário = 100 + 500 = 600 pontos
        self.assertEqual(calcular_pontos(valor=100.0, categoria='NORMAL', aniversario=True), 600)

if __name__ == '__main__':
    unittest.main()
