# spuštění testů - python -m unittest
# import testovacího modulu
import unittest

# import třídy QuadraticEquation ze souboru quadratic_equation.py
from quadratic_equation import QuadraticEquation

# vytvoření testovací třídy, která dědí ze třídy TestCase
class TestQuadraticEquation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass # volá se před začátkem všech testů

    @classmethod
    def tearDownClass(cls):
        pass # volá se po ukončení všech testů

    def setUp(self):
        pass # volá se před začátkem každého testu

    def tearDown(self):
        # volá se po ukončení každého testu
        # v tomto případě vytvoří vždy novou kv. rovnici
        from quadratic_equation import QuadraticEquation
        QuadraticEquation = QuadraticEquation(1,2,3)

    # discriminant test
    def test_discriminant(self):
        
        # Equation with 1 real root
        QuaEq1 = QuadraticEquation(1,2,1)
        self.assertEqual(QuaEq1.discriminant(), 0)
        QuaEq2 = QuadraticEquation(4,-12,9)
        self.assertEqual(QuaEq2.discriminant(), 0)

        # Equation with 2 real roots
        QuaEq3 = QuadraticEquation(1,-14,20)
        self.assertEqual(QuaEq3.discriminant(), 116)
        QuaEq4 = QuadraticEquation(-1,-14,20)
        self.assertEqual(QuaEq4.discriminant(), 276)