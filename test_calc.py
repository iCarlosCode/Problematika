from fractions import Fraction
import unittest
from unittest import result
import calculator.operations as op
from tabs import completar_quadrado, split_equation



class TestOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.A = (1, 2, 3)
        self.B = (3, 2, 1)
        self.o = (0, 0, 0)

        self.ox = (1, 0, 0)
        self.oy = (0, 1, 0)
        self.oz = (0, 0, 1)

    def tearDown(self):
        pass
    
    

    def test_de_fogo_completar_quadrado(self):
        #completar_quadrado()
        pass
        #TODO vai receber o completar_eq do tabs.completar_quadrado

    def test_split_equation(self):
        self.assertEqual(['x²', '+2x', '+y²', '-6y', '=6'], split_equation('x² +2x + y² - 6y=6'))
        self.assertEqual(['x²', '+2x', '+y²', '-6y', '+2'], split_equation('x² +2x + y² - 6y + 2=0'))
        self.assertEqual(['x²', '-1/2x', '+y²', '-0.5y', '+2'], split_equation('x² -1/2x + y² - 0.5y + 2=0'))


    def test_obter_coeficiente(self):
        sample = ['x²', '2x', 'y²', '1/2y', '6']
        
        self.assertEqual(1, op.obter_coeficiente('x²', sample))
        self.assertEqual(2, op.obter_coeficiente('x', sample))
        self.assertEqual(1, op.obter_coeficiente('y²', sample))
        self.assertEqual(Fraction(1,2), op.obter_coeficiente('y', sample))
        self.assertEqual(6, op.obter_coeficiente('=', sample))


    def test_completar_quadrado(self):
        self.assertEqual("(x + 1)² = 1", op.completar_quadrado((1, 2)))
        self.assertEqual("(x - 1)² = 1", op.completar_quadrado((1, -2)))
        self.assertEqual("x² = 0", op.completar_quadrado((1, 0)))
        self.assertEqual("x² + y² = 0", op.completar_quadrado((1, 0), y = (1,0), F=0))
        self.assertEqual("(x + 1)² + (y - 3)² = 4", op.completar_quadrado((1, 2), y = (1,-6), F=6))
        self.assertEqual("(x - 3)² + (y + 4)² = 4", op.completar_quadrado((1, -6), y = (1,8), F=21))
        self.assertEqual("3(x + 3)² + 2(y - 2)² = 6", op.completar_quadrado((3, 18), y = (2,-8), F=29))

        self.assertEqual("3(x + 3)² = 27", op.completar_quadrado((3, 18)))
        self.assertEqual("2(x + 1)² = 2", op.completar_quadrado((2, 4)))
        self.assertEqual("(x + 3/2)² = 9/4", op.completar_quadrado((1, 3)))
        self.assertEqual("2(x + 1/2)² = 1/2", op.completar_quadrado((2, 2)))
        self.assertEqual("3(x + 1/3)² = 1/3", op.completar_quadrado((3, 2)))
        self.assertEqual("3(x + 5/6)² = 25/12", op.completar_quadrado((3, 5)))
        
        self.assertEqual("(x + 1)² + y = 1", op.completar_quadrado((1, 2), (None, 1)))

        with self.assertRaises(ValueError):
            op.completar_quadrado((0, 0))


    def test_obter_vetor_de_dois_pontos(self):
        self.assertTupleEqual((2, 0, -2), op.obterVetorDePontos(self.A, self.B))
        self.assertTupleEqual(self.B, op.obterVetorDePontos(self.o, self.B))

    def test_soma(self):
        self.assertTupleEqual((4, 4, 4), op.calcularSoma(self.A, self.B))
        self.assertTupleEqual(self.B, op.calcularSoma(self.o, self.B))
        self.assertTupleEqual(self.A, op.calcularSoma(self.A, self.o))
        self.assertTupleEqual((-3, 1, -2), op.calcularSoma((-1, -2, -1), (-2, 3, -1)))

    def test_subtração(self):
        self.assertTupleEqual((-2, 0, 2), op.calcularSubtração(self.A, self.B))
        self.assertTupleEqual((-3, -2, -1), op.calcularSubtração(self.o, self.B))
        self.assertTupleEqual(self.A, op.calcularSubtração(self.A, self.o))
        self.assertTupleEqual(
            (1, -5, 0), op.calcularSubtração((-1, -2, -1), (-2, 3, -1))
        )

    def test_paralelismo(self):
        self.assertEqual(False, op.checarParalelismo(self.ox, self.oy))
        self.assertEqual(False, op.checarParalelismo(self.ox, self.oz))
        self.assertEqual(False, op.checarParalelismo(self.oz, self.oy))
        self.assertEqual(False, op.checarParalelismo(self.oy, self.oz))
        self.assertEqual(True, op.checarParalelismo((3, -5, -1), (-3, 5, 1)))
        self.assertEqual(True, op.checarParalelismo((0, 0, 0), self.B))

    def test_perpedincularismo(self):
        self.assertEqual(True, op.checarPerpedincularismo(self.ox, self.oy))
        self.assertEqual(True, op.checarPerpedincularismo(self.ox, self.oz))
        self.assertEqual(True, op.checarPerpedincularismo(self.oz, self.oy))
        self.assertEqual(True, op.checarPerpedincularismo(self.oy, self.oz))
        self.assertEqual(False, op.checarPerpedincularismo((3, -5, -1), (-3, 5, 1)))
        self.assertEqual(True, op.checarPerpedincularismo((0, 0, 0), self.B))

    # Testes dos Produtos
    def test_produto_escalar(self):
        # self.assertEqual(, op.calcularProdutoEscalar((,,), (,,)))
        self.assertEqual(-35, op.calcularProdutoEscalar((3, -5, -1), (-3, 5, 1)))
        self.assertEqual(0, op.calcularProdutoEscalar((3, 1, -3), (2, -3, 1)))

    def test_produto_vetorial(self):
        self.assertTupleEqual(
            (-1, 2, 7), op.calcularProdutoVetorial((3, -2, 1), (2, 1, 0))
        )
        self.assertTupleEqual(
            self.o, op.calcularProdutoVetorial((1, -1, -1), (-1, 1, 1))
        )
        self.assertTupleEqual(
            (-3, -2, 1), op.calcularProdutoVetorial((1, 0, 3), (-1, 1, -1))
        )
        self.assertTupleEqual(
            (4, 4, 8), op.calcularProdutoVetorial((1, -3, 1), (3, -1, -1))
        )

    def test_produto_misto(self):
        #       self.assertTupleEqual(2, op.calcularProdutoMisto((,,), (,,), (,,)))

        self.assertEqual(2, op.calcularProdutoMisto((-1, 4, -1), (3, -2, 1), (2, 1, 0)))
        self.assertEqual(
            31, op.calcularProdutoMisto((-3, -2, 4), (1, -2, 3), (4, 3, -2))
        )
        self.assertEqual(
            -2, op.calcularProdutoMisto((-1, -1, 0), (1, 2, -1), (2, 0, 4))
        )
        self.assertEqual(
            0, op.calcularProdutoMisto((1, 0, -2), (1, 2, 4), (-1, -1, -1))
        )

    # Posição Relativa
    def test_pos_relativa_duas_retas(self):
        # self.assertEqual('', op.calcularPosRelativaDuasRetas((,,), (,,), (,,), (,,)))
        self.assertEqual(
            "coincidentes",
            op.calcularPosRelativaDuasRetas((0, 0, 0), self.ox, (0, 0, 0), self.ox),
        )
        self.assertEqual(
            "concorrentes",
            op.calcularPosRelativaDuasRetas((0, 0, 0), self.ox, (0, 0, 0), self.oy),
        )
        self.assertEqual(
            "distintas",
            op.calcularPosRelativaDuasRetas((5, 1, -2), self.ox, (0, 0, 0), self.ox),
        )
        self.assertEqual(
            "reversas",
            op.calcularPosRelativaDuasRetas((1, -2, 5), (1, 2, 3), (0, 0, 0), self.ox),
        )


if __name__ == "__main__":
    unittest.main()
