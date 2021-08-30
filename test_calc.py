import unittest
from unittest import result
import calculator.operations as op
from fractions import Fraction


def valor_formatado(n):
    return f"+ {Fraction(n)}" if n >= 0 else f"- {Fraction(-1*n)}"


def completar_quadrado(x, y = None, z = None, F = 0):
    icognitas = {}
    if x:
        icognitas['x'] = {"a": x[0], "b": x[1], "c": 0, 'd':1, 'expr':''}
    if y:
        icognitas['y'] = {"a": y[0], "b": y[1], "c": 0, 'd':1, 'expr':''}
    if z:
        icognitas['z'] = {"a": z[0], "b": z[1], "c": 0, 'd':1, 'expr':''}
    dictio = {
        "x": {"a": 0, "b": 0, "c": 0, 'd':1},
        "y": {"a": 0, "b": 0, "c": 0, 'd':1},
        "z": {"a": 0, "b": 0, "c": 0, 'd':1},
    }
    """
    [] ax = 0
    [x] ax = 1 e bx é divisível por 2
    [x] ax = 1 e bx não é divisível por 2

    [x] ax != 1 e bx é divisível por ax e depois por 2
    [x] ax != 1 e bx é divisível por ax e depois não por 2

    [x] ax != 1 e bx não é divisível por ax mas é por 2
    [x] ax != 1 e bx não é divisível por ax e nem por 2
    """
    resultado = ""

    for i in icognitas.values():
        i['d'] = i['a']
        i['b'] = Fraction(i['b'], i['a'])
        i['b'] = Fraction(i['b'], 2)
        i['c'] = i['d']*(i['b']**2)
        i['a'] = Fraction(i['a'], i['a'])

        if i['b'] == 0:
            i['expr'] = f"x²"
        else:
            i['expr'] = f"{'' if i['d'] == 1 else i['d']}(x {valor_formatado(i['b'])})²"

    for i in icognitas.values():
        resultado += f"{i['expr']}" if resultado == '' else (f" + {i['expr']}" if i['d'] >= 0 else f" - {i['expr']}")
        F += i['c']
    print(f'{resultado} = {F}')
    return f'{resultado} = {F}'


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

    def test_completar_quadrado(self):
        self.assertEqual("(x + 1)² = 1", completar_quadrado((1, 2)))
        self.assertEqual("(x - 1)² = 1", completar_quadrado((1, -2)))
        self.assertEqual("x² = 0", completar_quadrado((1, 0)))
        self.assertEqual("x² = 0", completar_quadrado((1, 0), y = (1,0), F=0))

        self.assertEqual("3(x + 3)² = 27", completar_quadrado((3, 18)))
        self.assertEqual("2(x + 1)² = 2", completar_quadrado((2, 4)))
        self.assertEqual("(x + 3/2)² = 9/4", completar_quadrado((1, 3)))
        self.assertEqual("2(x + 1/2)² = 1/2", completar_quadrado((2, 2)))
        self.assertEqual("3(x + 1/3)² = 1/3", completar_quadrado((3, 2)))
        self.assertEqual("3(x + 5/6)² = 25/12", completar_quadrado((3, 5)))
        



        #self.assertEqual("ax = 1 e bx não é divisível por 2", completar_quadrado(1, 1, 0))
        #self.assertEqual("ax != 1 e bx é divisível por ax e depois por 2", completar_quadrado(2, 4, 0))
        #self.assertEqual("ax != 1 e bx é divisível por ax e depois não por 2", completar_quadrado(2, 2, 0))
        #self.assertEqual("ax != 1 e bx não é divisível por ax mas é por 2", completar_quadrado(3, 2, 0))
        #self.assertEqual("ax != 1 e bx não é divisível por ax e nem por 2", completar_quadrado(3, 5, 0))


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
