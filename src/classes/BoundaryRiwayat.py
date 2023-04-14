import sqlite3
from .RiwayatPerjalanan import *
from .MetodeTransportasi import *
from .DestinasiWisata import *

class BoundaryRiwayat:
    def __init__(self):
        self.listRiwayat = []
        conn = sqlite3.connect('./database/kitabisajalan.db')
        c = conn.cursor()
        query = "select * from riwayatperjalanan"
        c.execute(query)
        riwayat = c.fetchall()
        for r in riwayat:
            listDestinasi = []
            listTransport = []
            q1 = """
            select ID_Transportasi, Jenis_Transportasi, Harga_Transportasi
            from transportPilihan natural join transportasi
            where ID_Riwayat = ?
            """
            c.execute(q1, (r[0],))
            transport = c.fetchall()

            for t in transport:
                listTransport.append(metodeTransportasi(t[0], t[1], t[2]))
            
            q2 = """
            select ID_Destinasi, Lokasi_Wisata, Daerah
            from destinasiPerjalanan inner join lokasiwisata on ID_Destinasi = ID_Wisata
            where ID_Perjalanan = ?
            """

            c.execute(q2, (r[0],))
            destinasi = c.fetchall()

            for d in destinasi:
                listDestinasi.append(DestinasiWisata(d[0], d[1], d[2]))

            q3 = """
            select isi 
            from catatan
            where ID_Catatan = ?
            """

            c.execute(q3, (r[1],))
            catatan = c.fetchall()

            self.listRiwayat.append(RiwayatPerjalanan(r[0], r[1], r[2], r[3], r[4], listDestinasi, listTransport, catatan[0][0]))
        
        conn.close()

    def getRiwayat(self, idx = None):
        if(idx == None):
            return self.listRiwayat
        else:
            for r in self.listRiwayat:
                if(r.get_id_riwayat() == idx):
                    return r
            
            return 0
