import unittest
from classes import *

class Test(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.listDestinasiWisata = BoundaryDestinasiWisata().getList()
    
    def test_getList(self):
        self.assertEqual(len(self.listDestinasiWisata), 16)
    
    # def test_printAll(self):
    #     self.assertEqual(self.listDestinasiWisata[0].printAll(), "1. Jakarta")
    #     self.assertEqual(self.listDestinasiWisata[1].printAll(), "2. Bandung")

if __name__ == "__main__":
    unittest.main()