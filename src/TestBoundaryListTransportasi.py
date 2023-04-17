import unittest
from classes import *

class TestBoundaryListTransportasi(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.listTransportasiPilihan = BoundaryListTransportasi().getList()
    
    def test_addToPerjalanan(self):
        self.assertEqual(len(self.listTransportasiPilihan), 0)
        self.listTransportasiPilihan.append(metodeTransportasi(1, "Kereta", 50000))
        self.assertEqual(len(self.listTransportasiPilihan), 1)
    
    def test_getList(self):
        self.assertEqual(len(self.listTransportasiPilihan), 1) #gangerti dia ttp kosong

    def test_printAll(self):
        self.assertEqual(self.listTransportasiPilihan[0].getID(), 1)
        self.assertEqual(self.listTransportasiPilihan[0].getNama(), "Kereta")
        self.assertEqual(self.listTransportasiPilihan[0].getHarga(), 50000)

if __name__ == "__main__":
    unittest.main()