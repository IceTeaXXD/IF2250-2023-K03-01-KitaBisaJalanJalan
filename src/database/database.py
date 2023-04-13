import sqlite3

def init_Database():
    conn = sqlite3.connect('kitabisajalan.db')
    c = conn.cursor()

    q1 = """CREATE TABLE IF NOT EXISTS daerah(
        ID_Daerah INTEGER,
        Daerah TEXT,
        Lokasi_Koordinat TEXT,
        PRIMARY KEY(ID_Daerah)
        )"""

    q2 = """
    create table IF NOT EXISTS catatan(
        ID_Catatan INTEGER,
        tgl_mulai TEXT,
        tgl_akhir TEXT,
        isi TEXT,
        PRIMARY KEY(ID_Catatan)
        )
    """

    q3 = """
    create table IF NOT EXISTS lokasiwisata(
        `ID_Wisata` INTEGER,
        `Lokasi_Wisata` TEXT,
        `Lokasi_Koordinat` TEXT,
        `Daerah` INTEGER,
        PRIMARY KEY(`ID_Wisata`),
        FOREIGN KEY (`Daerah`) REFERENCES daerah(`ID_Daerah`)
        )
    """

    q4 = """
    create table IF NOT EXISTS transportasi(
        `ID_Transportasi` integer,
        `Jenis_Transportasi` text,
        `Harga_Transportasi` integer,
        PRIMARY KEY(`ID_Transportasi`)
    )
    """

    q5 = """
    create table IF NOT EXISTS riwayatperjalanan(
        `ID_riwayat` INTEGER,
        `ID_Perjalanan` INTEGER,
        `tgl_mulai` TEXT,
        `tgl_akhir` TEXT,
        `biaya_perjalanan` INTEGER,
        PRIMARY KEY (`ID_riwayat`),
        FOREIGN KEY (`ID_Perjalanan`) REFERENCES catatan(`ID_Catatan`)
    )
    """

    q6 = """
    create table IF NOT EXISTS destinasiPerjalanan(
    `ID_Perjalanan` INTEGER,
    `ID_Destinasi` INTEGER,
    PRIMARY KEY (`ID_Perjalanan`, `ID_Destinasi`),
    FOREIGN KEY (`ID_Perjalanan`) REFERENCES riwayatperjalanan(`ID_Perjalanan`),
    FOREIGN KEY (`ID_Destinasi`) REFERENCES lokasiwisata(`ID_Wisata`)
    )
    """

    q7 = """
    create table IF NOT EXISTS transportPilihan(
        `ID_Riwayat` INTEGER,
        `ID_Transportasi` INTEGER,
        PRIMARY KEY(`ID_Riwayat`, `ID_Transportasi`),
        FOREIGN KEY (`ID_Riwayat`) REFERENCES riwayatperjalanan(`ID_riwayat`),
        FOREIGN KEY (`ID_Transportasi`) REFERENCES transportasi(`ID_Transportasi`)
    )
    """

    q8 = """
    insert into daerah(ID_Daerah, Daerah, Lokasi_Koordinat) values 
    (1, 'Jakarta', '10'), 
    (2, 'Bandung', '11'), 
    (3, 'Bali', '12')
    """
    
    q9 = """
    insert into lokasiwisata values
    (1, 'Dufan', '10', 1),
    (2, 'Pantai Ancol', '10', 1),
    (3, 'PVJ', '10', 2),
    (4, 'Orchid Forest', 15, 2),
    (5, 'Pantai Kuta', 30, 3),
    (6, 'Pura Ulun Danu Brata', 35, 3)
    """

    q10 = """
    insert into transportasi values
    (1, 'Mobil', 10000),
    (2, 'Motor', 5000),
    (3, 'Kereta', 50000),
    (4, 'Pesawat', 1000000)
    """
    with conn:
        c.execute(q1)
        c.execute(q2)
        c.execute(q3)
        c.execute(q4)
        c.execute(q5)
        c.execute(q6)
        c.execute(q7)
        c.execute(q8)
        c.execute(q9)
        c.execute(q10)

    conn.close()

init_Database()
print("Sukses")