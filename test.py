import unittest
from main import suma
from main import resta
class TestPrueba(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3, 4), 7)
    
    def test_resta(self):
        self.assertEqual(resta(10, 2), 8)

if __name__ == "__main__":
    unittest.main()