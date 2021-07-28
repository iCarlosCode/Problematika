import unittest
from unittest import result
import calculator.operations as op

class TestOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.A = (1,2,3)
        self.B = (3,2,1)
        self.o = (0,0,0)

        self.ox = (1,0,0)
        self.oy = (0,1,0)
        self.oz = (0,0,1)

    def tearDown(self):
        pass

    def test_obter_vetor_de_dois_pontos(self):
        self.assertTupleEqual((2,0,-2), op.obterVetorDePontos(self.A, self.B))
        self.assertTupleEqual(self.B, op.obterVetorDePontos(self.o, self.B))


    def test_soma(self):
        self.assertTupleEqual((4,4,4), op.calcularSoma(self.A, self.B))
        self.assertTupleEqual(self.B, op.calcularSoma(self.o, self.B))
        self.assertTupleEqual(self.A, op.calcularSoma(self.A, self.o))
        self.assertTupleEqual((-3,1,-2), op.calcularSoma((-1, -2, -1), (-2, 3, -1)))

    def test_subtração(self):
        self.assertTupleEqual((-2,0,2), op.calcularSubtração(self.A, self.B))
        self.assertTupleEqual((-3,-2,-1), op.calcularSubtração(self.o, self.B))
        self.assertTupleEqual(self.A, op.calcularSubtração(self.A, self.o))
        self.assertTupleEqual((1,-5,0), op.calcularSubtração((-1, -2, -1), (-2, 3, -1)))

    def test_paralelismo(self):
        self.assertEqual(False, op.checarParalelismo(self.ox, self.oy))
        self.assertEqual(False, op.checarParalelismo(self.ox, self.oz))
        self.assertEqual(False, op.checarParalelismo(self.oz, self.oy))
        self.assertEqual(False, op.checarParalelismo(self.oy, self.oz))
        self.assertEqual(True, op.checarParalelismo((3,-5,-1), (-3,5,1)))
        self.assertEqual(True, op.checarParalelismo((0,0,0), self.B))

        
    def test_perpedincularismo(self):
        self.assertEqual(True, op.checarPerpedincularismo(self.ox, self.oy))
        self.assertEqual(True, op.checarPerpedincularismo(self.ox, self.oz))
        self.assertEqual(True, op.checarPerpedincularismo(self.oz, self.oy))
        self.assertEqual(True, op.checarPerpedincularismo(self.oy, self.oz))
        self.assertEqual(False, op.checarPerpedincularismo((3,-5,-1), (-3,5,1)))
        self.assertEqual(True, op.checarPerpedincularismo((0,0,0), self.B))

    # Testes dos Produtos
    def test_produto_escalar(self):
        #self.assertEqual(, op.calcularProdutoEscalar((,,), (,,)))  
        self.assertEqual(-35, op.calcularProdutoEscalar((3,-5,-1), (-3,5,1)))
        self.assertEqual(0, op.calcularProdutoEscalar((3,1,-3), (2,-3,1)))

    def test_produto_vetorial(self):
        self.assertTupleEqual((-1,2,7), op.calcularProdutoVetorial((3,-2,1),(2,1,0)))
        self.assertTupleEqual(self.o, op.calcularProdutoVetorial((1,-1,-1),(-1,1,1)))
        self.assertTupleEqual((-3,-2,1), op.calcularProdutoVetorial((1,0,3),(-1,1,-1)))
        self.assertTupleEqual((4,4,8), op.calcularProdutoVetorial((1,-3,1),(3,-1,-1)))

    def test_produto_misto(self):
 #       self.assertTupleEqual(2, op.calcularProdutoMisto((,,), (,,), (,,)))

        self.assertEqual(2, op.calcularProdutoMisto((-1,4,-1), (3,-2,1), (2,1,0)))
        self.assertEqual(31, op.calcularProdutoMisto((-3,-2,4), (1,-2,3), (4,3,-2)))
        self.assertEqual(-2, op.calcularProdutoMisto((-1,-1,0), (1,2,-1), (2,0,4)))
        self.assertEqual(0, op.calcularProdutoMisto((1,0,-2), (1,2,4), (-1,-1,-1)))



    # Posição Relativa
    def test_pos_relativa_duas_retas(self):
        #self.assertEqual('', op.calcularPosRelativaDuasRetas((,,), (,,), (,,), (,,)))
        self.assertEqual('coincidentes', op.calcularPosRelativaDuasRetas((0,0,0), self.ox, (0,0,0),self.ox))
        self.assertEqual('concorrentes', op.calcularPosRelativaDuasRetas((0,0,0), self.ox, (0,0,0),self.oy))
        self.assertEqual('distintas', op.calcularPosRelativaDuasRetas((5,1,-2), self.ox, (0,0,0),self.ox))
        self.assertEqual('reversas', op.calcularPosRelativaDuasRetas((1,-2,5), (1,2,3), (0,0,0),self.ox))



if __name__ == '__main__':
    unittest.main()