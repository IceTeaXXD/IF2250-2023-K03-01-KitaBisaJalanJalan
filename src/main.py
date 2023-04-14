from classes import *

print("Please Select Your Action")
print("1. Lihat Destinasi")
print("2. Buat Perjalanan")
print("3. Lihat Riwayat")
print("4. Tambah Catatan")
print("5. Exit")

action = int(input(">> "))
while(action != 5):
    if(action == 1):
        listDaerah = BoundaryDaerahWisata()
        
        # Print listDaerah
        print("List Daerah yang Tersedia")
        listDaerah.printAll()

        # Choose
        print("Pilih dong daerahnya: ")
        idx = int(input(">> "))

        # Cari semua destinasi di daerah idx
        daerahPilihan = listDaerah.getDaerah(idx)
        print("Destinasi di",  daerahPilihan.getNama())

        # Kelas Boundary List Destinasi
        listDestinasi = BoundaryListDestinasi(daerahPilihan.getListDestinasiFromDaerah())
        listDestinasi.printAll()

    elif (action == 2):
        print("Mau berangkat tanggal berapa? (format: DD-MM-YYYY)")
        tanggalAwal = input(">> ")

        print("Mau selesai tanggal berapa? (format: DD-MM-YYYY)")
        tanggalAkhir = input(">> ")

        listDaerah = BoundaryDaerahWisata()
        
        # Print listDaerah
        print("List Daerah yang Tersedia")

        listDaerah.printAll()

        # Choose
        print("Pilih dong daerahnya: ")
        idx = int(input(">> "))

        # Cari semua destinasi di daerah idx
        daerahPilihan = listDaerah.getDaerah(idx)
        print("Destinasi di",  daerahPilihan.getNama())

        # Kelas Boundary List Destinasi
        listDestinasi = BoundaryListDestinasi(daerahPilihan.getListDestinasiFromDaerah())
        listDestinasi.printAll()

        # Kelas BoundaryDestinasiWisata -> Pilihan user
        listDestinasiPilihan = BoundaryDestinasiWisata()

        print("Pilih mau kemana aja kakak!")
        inputDest = int(input(">> "))
        while inputDest != -9999:
            listDestinasiPilihan.addToDestinasiPilihan(listDestinasi.getDestinasi(inputDest))
            inputDest = int(input(">> "))

        print("List destinasi Kakak ini nih:")
        listDestinasiPilihan.printAll()

        # Pemilihan Transportasi
        print("Pilih Transportnya Dulu Kakak :D")

        # Seharusnya ini ListTransportasi (sheesh salah bikin gw (PLAK PLAK GAMPAR GAMPAR))
        transportList = ListTransportasi()
        transportList.printAll()

        # Seharusnya ini BoundaryListTransportasi
        transportPilihan = BoundaryListTransportasi()
        inputTransport = int(input(">> "))
        while inputTransport != -9999:
            transportPilihan.addToPerjalanan(transportList.getTransportasi(inputTransport))
            inputTransport = int(input(">> "))

        print("Transportasinya Kakak")
        transportPilihan.printAll()

        # Hitung Biaya Perjalanan -> Kelas Controller Biaya Perjalanan
        # Basically ya kalkulasi aja sih, gampangnya sum of semua transport yang dipake

        controllerBiaya = ControllerBiayaTransportasi(transportPilihan.getList())
        biayaTransport = controllerBiaya.hitungBiaya()

        print("Biaya transportnya kakak", biayaTransport)

        # Sekarang ke Controller Perjalanan
        # di kelas ini kita buat listTransportasi dan listDestinasiPilihan
        # dimasukin ke tabel riwayatPerjalanan, destinasiPerjalanan, transportPilihan
        add = ControllerPerjalanan(biayaTransport, listDestinasiPilihan.getList(), transportPilihan.getList(), tanggalAwal, tanggalAkhir)
        add.makePerjalanan()

    elif (action == 3):
        print("Riwayat Perjalanan Anda")
        riwayat = BoundaryRiwayat()
        for r in riwayat.getRiwayat():
            r.print()
            print()

    elif (action == 4):
        print("Pilih Riwayat Perjalanan!")
        riwayat = BoundaryRiwayat()
        for r in riwayat.getRiwayat():
            print(r.get_id_riwayat())

        pilih = int(input(">> "))

        catatan = riwayat.getRiwayat(pilih)

        editCatatan = controllerCatatan(catatan.get_id_catatan(), catatan.get_catatan())

        # Minta catatan yang baru
        print("Masukkan catatan Anda: ")
        newCatatan = input(">> ")

        editCatatan.saveCatatan(newCatatan)
        editCatatan.submitCatatan()

    print("\nPlease Select Your Action")
    print("1. Lihat Destinasi")
    print("2. Buat Perjalanan")
    print("3. Lihat Riwayat")
    print("4. Tambah Catatan")
    print("5. Exit")
    action = int(input(">> "))