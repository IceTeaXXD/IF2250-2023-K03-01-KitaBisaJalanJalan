import sqlite3
from classes import *
import unittest

class TestControllerPerjalanan(unittest.TestCase):
    def test_makePerjalanan(self):
        perjalanan = ControllerPerjalanan(1055000, [DestinasiWisata(8, "Paskal 23", 2, "Macet bet ini tempat", "paskal.jpg"), DestinasiWisata(6, "PVJ", 2, "Ini mall gess", "pvj.jpg")], [metodeTransportasi(2, "Pesawat", 1000000), metodeTransportasi(1, "Kereta", 50000), metodeTransportasi(3, "Bus", 5000)], '2023-04-25', '2023-04-30')
        perjalanan.makePerjalanan()

        # cek apakah data sudah masuk ke dalam database
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        c.execute("select * from riwayatperjalanan where tgl_mulai=?", ('2023-04-25',))
        result = c.fetchone()
        conn.close()
        self.assertEqual(result, (49, 49, '2023-04-25', '2023-04-30', 1055000))
        
if __name__ == '__main__':
    unittest.main()