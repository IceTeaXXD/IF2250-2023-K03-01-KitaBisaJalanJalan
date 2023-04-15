import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from classes import ListTransportasi

class PerkiraanBiayaTransportasiWindow(QDialog):
    def __init__(self):
        super(PerkiraanBiayaTransportasiWindow, self).__init__()
        loadUi("./interface/ui/perkiraanBiayaTransportasi.ui", self)

        listTransport = ListTransportasi()

        # Menampilkan harga per transportasi
        for t in listTransport.getList():
            if t.getNama() == "Kereta":
                # Kasih Harganya
                self.harga_kereta.setText(str(t.getHarga()))
            elif (t.getNama() == "Mobil"):
                # Kasih Harganya
                self.harga_mobil.setText(str(t.getHarga()))
            elif (t.getNama() == "Pesawat"):
                # Kasih Harganya
                self.harga_pesawat.setText(str(t.getHarga()))
            else:
                # Kasih Harganya
                self.harga_bus.setText(str(t.getHarga()))

        # Nanti buat tiap object radioButton
        # dicek is set or not
        # kalo is set, pass ID via getID()
