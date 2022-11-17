import unittest

import parameterized as parameterized

import ConvertisseurNombresRomains


class MyTestCase(unittest.TestCase):

    @parameterized.parameterized.expand([[1], [2], [3]])
    def test_1_2_3(self, n):
        result = ConvertisseurNombresRomains.convertir(n)
        attendu = 'I'*n
        self.assertEqual(attendu, result)
    def test_4(self):
        nombre = 4
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('IV', result)

    @parameterized.parameterized.expand([[5], [6], [7], [8]])
    def test_5_6_7_8(self, n):
        result = ConvertisseurNombresRomains.convertir(n)
        attendu = 'V' + 'I' * (n - 5)
        self.assertEqual(attendu, result)
    def test_9(self):
        nombre = 9
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('IX', result)
    def test_10(self):
        nombre = 10
        result = ConvertisseurNombresRomains.convertir(nombre)
        self.assertEqual('X', result)



if __name__ == '__main__':
    unittest.main()
