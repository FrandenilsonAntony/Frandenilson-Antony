import unittest
from calculator_python import calculator

class TestCalculator(unittest.TestCase):
    def test_calculator(self):
        result = calculator(10000, 11000, 12000, 0.10, 'Residencial')
        self.assertAlmostEqual(result[0], 2970)
        self.assertAlmostEqual(result[1], 247.5)
        self.assertAlmostEqual(result[2], 0.22)
        self.assertAlmostEqual(result[3], 0.95)

if __name__ == '__main__':
    unittest.main()