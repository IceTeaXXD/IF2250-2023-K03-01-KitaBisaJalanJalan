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
        self.assertEqual(self.listDaerahWisata[9].getID(), 2)
        self.assertEqual(self.listDaerahWisata[9].getNama(), "Bandung")
    
    def test_printAll(self):
        self.assertEqual(self.listDaerahWisata[0].print(), "1. Jakarta")
        self.assertEqual(self.listDaerahWisata[9].print(), "2. Bandung")


if __name__ == "__main__":
    unittest.main()