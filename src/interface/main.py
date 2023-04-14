import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

import home as home
import catatan as catatan
import pilihDaerah as pilihDaerah
import pilihDestinasi as pilihDestinasi
import riwayatPerjalanan as riwayatPerjalanan
import perkiraanBiayaTransportasi as perkiraanBiayaTransportasi
import sedangBerlangsung as sedangBerlangsung
import pilihTanggalPerjalanan as pilihTanggalPerjalanan
import image

class MainApplication(QApplication):
    def __init__(self, argv):
        super(MainApplication, self).__init__(argv)
        self.home = home.HomeWindow()
        self.catatan = catatan.CatatanWindow()
        self.pilihDaerah = pilihDaerah.pilihDaerahWindow()
        self.pilihDestinasi = pilihDestinasi.pilihDestinasiWindow()
        self.riwayatPerjalanan = riwayatPerjalanan.riwayatPerjalananWindow()
        self.perkiraanBiayaTransportasi = perkiraanBiayaTransportasi.PerkiraanBiayaTransportasiWindow()
        self.sedangBerlangsung = sedangBerlangsung.sedangBerlangsungWindow()
        self.pilihTanggalPerjalanan = pilihTanggalPerjalanan.pilihTanggalPerjalananWindow()
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.home)
        self.widget.addWidget(self.catatan)
        self.widget.addWidget(self.pilihDaerah)
        self.widget.addWidget(self.pilihDestinasi)
        self.widget.addWidget(self.riwayatPerjalanan)
        self.widget.addWidget(self.perkiraanBiayaTransportasi)
        self.widget.addWidget(self.sedangBerlangsung)
        self.widget.addWidget(self.pilihTanggalPerjalanan)
        self.widget.setFixedWidth(1512)
        self.widget.setFixedHeight(982)
        self.widget.show()
        self.home.button_baru.clicked.connect(self.button_baru_clicked)
        self.pilihDaerah.back_button.clicked.connect(self.pilihDaerah_back_button_clicked)
        self.pilihDaerah.next_button.clicked.connect(self.pilihDaerah_next_button_clicked)
        self.pilihDestinasi.back_button.clicked.connect(self.pilihDestinasiback_button_clicked)
        self.pilihDestinasi.next_button.clicked.connect(self.pilihDestinasinext_button_clicked)
        self.perkiraanBiayaTransportasi.back_button.clicked.connect(self.perkiraanBiayaTransportasi_back_button_clicked)
        self.perkiraanBiayaTransportasi.next_button.clicked.connect(self.perkiraanBiayaTransportasi_next_button_clicked)
        self.riwayatPerjalanan.back_button.clicked.connect(self.riwayatPerjalanan_back_button_clicked)
        self.catatan.back_button.clicked.connect(self.back_button_clicked)  
        self.pilihTanggalPerjalanan.back_button.clicked.connect(self.pilihTanggalPerjalanan_back_button_clicked)
        self.pilihTanggalPerjalanan.submit.clicked.connect(self.submit_clicked)
        self.sedangBerlangsung.back_button.clicked.connect(self.sedangBerlangsung_back_button_clicked)
        self.home.button_riwayat.clicked.connect(self.button_riwayat_clicked)
        self.home.button_sedangberlangsung.clicked.connect(self.sedangberlangsung_clicked)

    def button_baru_clicked(self):
        self.widget.setCurrentWidget(self.pilihDaerah)
    def pilihDaerah_next_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihDestinasi)
    def pilihDaerah_back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)
    def pilihDestinasiback_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihDaerah)
    def pilihDestinasinext_button_clicked(self):
        self.widget.setCurrentWidget(self.perkiraanBiayaTransportasi)
    def perkiraanBiayaTransportasi_back_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihDestinasi)
    def perkiraanBiayaTransportasi_next_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihTanggalPerjalanan)
    def button_riwayat_clicked(self):
        self.widget.setCurrentWidget(self.riwayatPerjalanan)
    def sedangberlangsung_clicked(self):
        self.widget.setCurrentWidget(self.sedangBerlangsung)
    def sedangBerlangsung_back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)
    def riwayatPerjalanan_back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)
    def back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)
    def pilihTanggalPerjalanan_back_button_clicked(self):
        self.widget.setCurrentWidget(self.perkiraanBiayaTransportasi)
    def submit_clicked(self):
        self.widget.setCurrentWidget(self.home)

run = MainApplication(sys.argv)
sys.exit(run.exec_())