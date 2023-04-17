import unittest
import os
import sys
from classes import *

class Test(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.listDaerahWisata = BoundaryDaerahWisata().getListDaerah()
    
    def test_getListDaerah(self):
        self.assertEqual(len(self.listDaerahWisata), 3)

    def test_getDaerah(self):
        self.assertEqual(self.listDaerahWisata[0].getID(), 1)
        self.assertEqual(self.listDaerahWisata[0].getNama(), "Jakarta")
        self.assertEqual(self.listDaerahWisata[1].getID(), 2)
        self.assertEqual(self.listDaerahWisata[1].getNama(), "Bandung")
    
    def test_printAll(self):
        self.assertEqual((self.listDaerahWisata[0].getID(), "\b. ", self.listDaerahWisata[0].getNama()), (1, "\b. ", "Jakarta"))
        self.assertEqual((self.listDaerahWisata[1].getID(), "\b. ", self.listDaerahWisata[1].getNama()), (2, "\b. ", "Bandung"))


if __name__ == "__main__":
    unittest.main()