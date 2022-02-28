import unittest

def multiplicacion(num1, num2):
    return num1*num2

class CajaNegra(unittest.TestCase):
    def test_multiplica_dos_positivo(self):
        num_1 = 3
        num_2 = 4
        resultado = multiplicacion(num_1, num_2)
        self.assertEqual(resultado, 12)

    def test_multiplica_dos_negativo(self):
        num_1=-10
        num_2=-7
        resultado = multiplicacion(num_1, num_2)
        self.assertEqual(resultado,70)

    def test_multiplica_positivo_negativo(self):
        num_1=-10
        num_2=7
        resultado = multiplicacion(num_1, num_2)
        self.assertEqual(resultado,-70)

if __name__ == "__main__":
    unittest.main()