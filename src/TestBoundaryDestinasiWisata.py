import unittest
from classes import *

class TestBoundaryDestinasiWisata(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.listDestinasiPilihan = BoundaryDestinasiWisata().getList()

    def test_getList(self):
        self.assertEqual(len(self.listDestinasiPilihan), 0) # dia gamau masuk ke listnya (aneh)
        
    def test_addToDestinasiPilihan(self):
        self.listDestinasiPilihan.append(DestinasiWisata(1, "Dufan", "1", "Tempat bermain anak"))
        self.listDestinasiPilihan.append(DestinasiWisata(2, "Pantai Ancol", "1", "Tempat pantai anak"))
        self.assertEqual(len(self.listDestinasiPilihan), 2)
    
    def test_printAll(self):
        self.assertEqual((self.listDestinasiPilihan[0].getID(), "\b. ", self.listDestinasiPilihan[0].getNama()), (1, "\b. ", "Dufan 1, Tempat bermain anak"))
        self.assertEqual((self.listDestinasiPilihan[1].getID(), "\b. ", self.listDestinasiPilihan[1].getNama()), (2, "\b. ", "Pantai Ancol, 1, Tempat pantai anak"))

if __name__ == "__main__":
    unittest.main()