import unittest
import ConvertisseurNombresRomains


class MyTestCase(unittest.TestCase):
    def test_one(self):
        nombre = 1
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('I', result)
    def test_two(self):
        nombre = 2
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('II', result)
    def test_three(self):
        nombre = 3
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('III', result)
    def test_four(self):
        nombre = 4
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('IV', result)
    def test_five(self):
        nombre = 5
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('V', result)
    def test_six(self):
        nombre = 6
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('VI', result)
    def test_seven(self):
        nombre = 7
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('VII', result)
    def test_eight(self):
        nombre = 8
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('VIII', result)
    def test_nine(self):
        nombre = 9
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('IX', result)
    def test_ten(self):
        nombre = 10
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('X', result)



if __name__ == '__main__':
    unittest.main()
