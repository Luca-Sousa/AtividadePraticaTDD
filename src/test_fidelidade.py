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

if __name__ == '__main__':
    unittest.main()
