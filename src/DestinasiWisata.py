class DestinasiWisata:
    # Konstruktor Destinasi Wisata 
    def __init__(self, idDestinasi, destinasi, daerah):
        self.__idDestinasi = idDestinasi
        self.__destinasi = destinasi
        self.__daerah = daerah
    
    # Mengembalikan sebuah tipe Destinasi Wisata yang
    # nantinya dapat di-append ke suatu list yang lebih besar
    # untuk dijadikan array pilihan
    def makeList(self):
        return [self.__idDestinasi, self.__destinasi, self.__daerah]
    
    def getID(self):
        return self.__idDestinasi
    
    def getNamaDestinasi(self):
        return self.__destinasi