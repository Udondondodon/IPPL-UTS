import unittest
from mathcode import *

class TestGeometryFunctions(unittest.TestCase):
    def test_luas_persegi(self):
        self.assertEqual(luas_persegi(5), 25)
        self.assertEqual(luas_persegi(0), 0)
        self.assertEqual(luas_persegi(-3), 9)

    def test_keliling_persegi_panjang(self):
        self.assertEqual(keliling_persegi_panjang(5, 4), 18)
        self.assertEqual(keliling_persegi_panjang(2, 10), 24)
        self.assertEqual(keliling_persegi_panjang(3, 6), 18)

    def test_luas_segitiga(self):
        self.assertEqual(luas_segitiga(6, 8), 24)
        self.assertEqual(luas_segitiga(2, 10), 10)
        self.assertEqual(luas_segitiga(3, 4), 6)

    def test_panjang_sisi_miring_segitiga(self):
        self.assertAlmostEqual(panjang_sisi_miring_segitiga(3, 4), 5)
        self.assertAlmostEqual(panjang_sisi_miring_segitiga(5, 12), 13)
        self.assertAlmostEqual(panjang_sisi_miring_segitiga(6, 8), 10)

    def test_keliling_segitiga(self):
        self.assertEqual(keliling_segitiga(2, 4, 8), 14)
        self.assertEqual(keliling_segitiga(6, 8, 10), 24)
        self.assertEqual(keliling_segitiga(5, 10, 15), 30)

if __name__ == '__main__':
    unittest.main()