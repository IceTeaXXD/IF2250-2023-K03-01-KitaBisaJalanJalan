import unittest
from classes import *

class TestBoundaryListDestinasi(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.listDestinasi = BoundaryListDestinasi().getList()
    
    # def test_printAll(self):
    #     self.assertEqual((self.listDestinasi[0].getID(), "\b. ", self.listDaerahWisata[0].getNama()), (1, "\b. ", "Dufan, 1, Tempat bermain anak"))
    #     self.assertEqual((self.listDestinasi[1].getID(), "\b. ", self.listDaerahWisata[1].getNama()), (2, "\b. ", "Pantai Ancol, 1, Tempat pantai anak"))
    
    # def test_getDestinasi(self):
    #     self.assertEqual(self.listDestinasi[0].getID(), 1)
    #     self.assertEqual(self.listDestinasi[0].getNamaDestinasi(), "Dufan")
    #     self.assertEqual(self.listDestinasi[0].getDeskripsi(), "Tempat bermain anak")
    #     self.assertEqual(self.listDestinasi[0].getDaerah(), 1)
    #     self.assertEqual(self.listDestinasi[1].getID(), 2)
    #     self.assertEqual(self.listDestinasi[1].getNamaDestinasi(), "Pantai Ancol")
    #     self.assertEqual(self.listDestinasi[1].getDeskripsi(), "Tempat pantai anak")
    #     self.assertEqual(self.listDestinasi[1].getDaerah(), 1)

    def test_getList(self):
        self.assertEqual(len(self.listDestinasi), 16)

if __name__ == "__main__":
    unittest.main()