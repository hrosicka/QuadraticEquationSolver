import os
import sys
# Import the testing module
import unittest

# Dynamically add the parent directory to sys.path
# This ensures the module can be imported regardless of the working directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the QuadraticEquation class from quadratic_equation.py
from quadratic_equation import QuadraticEquation

# Create a test class that inherits from TestCase
class TestQuadraticEquation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass # Called before all tests start

    @classmethod
    def tearDownClass(cls):
        pass # Called after all tests finish

    def setUp(self):
        pass # Called before each individual test

    def tearDown(self):
        # Called after each individual test
        pass

    # Discriminant tests
    def test_discriminant(self):
        
        # Equation with 1 real root
        qua_eq1 = QuadraticEquation(1, 2, 1)
        self.assertEqual(qua_eq1.discriminant(), 0)
        qua_eq2 = QuadraticEquation(4, -12, 9)
        self.assertEqual(qua_eq2.discriminant(), 0)

        # Equation with 2 real roots
        qua_eq3 = QuadraticEquation(1, -14, 20)
        self.assertEqual(qua_eq3.discriminant(), 116)
        qua_eq4 = QuadraticEquation(-1, -14, 20)
        self.assertEqual(qua_eq4.discriminant(), 276)

    def test_one_real_root(self):
        qe = QuadraticEquation(1, 2, 1)
        qe.solve()
        self.assertEqual(qe.x1, qe.x2)  # Oba kořeny jsou stejné
        
    def test_two_real_roots(self):
        qe = QuadraticEquation(1, -5, 6)
        qe.solve()
        self.assertAlmostEqual(qe.x1, 3.0, places=3)
        self.assertAlmostEqual(qe.x2, 2.0, places=3)

    def test_complex_roots(self):
        qe = QuadraticEquation(1, 2, 5)
        qe.solve()
        self.assertEqual(qe.x1.imag > 0, True)  # Má imaginární část
        
    def test_vertex_calculation(self):
        qe = QuadraticEquation(1, -4, 4)
        qe.solve()
        self.assertAlmostEqual(qe.vertex_x, 2.0, places=3)
        self.assertAlmostEqual(qe.vertex_y, 0.0, places=3)

if __name__ == "__main__":
    unittest.main()