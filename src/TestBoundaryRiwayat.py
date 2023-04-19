import unittest
from classes import *

class TestBoundaryRiwayat(unittest.TestCase):
    def test_getRiwayat(self):
        listRiwayat = BoundaryRiwayat().getRiwayat()
        self.assertEqual(len(listRiwayat), 0) # gak tau masi bingung

    def test_getRiwayatBerlangsung(self):
        listRiwayatBerlangsung = BoundaryRiwayat().getRiwayatBerlangsung()
        self.assertEqual(len(listRiwayatBerlangsung), 0) # ini juga gak tau


if __name__ == "__main__":
    unittest.main()