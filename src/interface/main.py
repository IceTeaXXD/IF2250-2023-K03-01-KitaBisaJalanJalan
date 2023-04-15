import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

from .home import *
from .catatan import *
from .pilihDaerah import *
from .pilihDestinasi import *
from .riwayatPerjalanan import *
from .perkiraanBiayaTransportasi import *
from .sedangBerlangsung import *
from .pilihTanggalPerjalanan import *
from .image import *

class MainApplication(QApplication):
    def __init__(self, argv):
        super(MainApplication, self).__init__(argv)

        # Initialize the windows
        self.home = HomeWindow()
        self.catatan = CatatanWindow()
        self.pilihDaerah = pilihDaerahWindow()
        self.pilihDestinasi = pilihDestinasiWindow()
        self.riwayatPerjalanan = riwayatPerjalananWindow()
        self.perkiraanBiayaTransportasi = PerkiraanBiayaTransportasiWindow()
        self.sedangBerlangsung = sedangBerlangsungWindow()
        self.pilihTanggalPerjalanan = pilihTanggalPerjalananWindow()
        
        # Initialize the widgets for the main window and pages
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.home)
        self.widget.addWidget(self.catatan)
        self.widget.addWidget(self.pilihDaerah)
        self.widget.addWidget(self.pilihDestinasi)
        self.widget.addWidget(self.riwayatPerjalanan)
        self.widget.addWidget(self.perkiraanBiayaTransportasi)
        self.widget.addWidget(self.sedangBerlangsung)
        self.widget.addWidget(self.pilihTanggalPerjalanan)
        
        # Set the main window size
        self.widget.setFixedWidth(1512)
        self.widget.setFixedHeight(982)
        self.widget.show()

        # Button Handlers
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
        if self.pilihDaerah.selectedID() == None:
            # error dialog box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Daerah Belum Dipilih!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        self.pilihDestinasi.reset()
        self.pilihDestinasi.setDaerah(self.pilihDaerah.daerahwisata.getDaerah(self.pilihDaerah.selectedID()).getListDestinasiFromDaerah())
        self.widget.setCurrentWidget(self.pilihDestinasi)

    def pilihDaerah_back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)

    def pilihDestinasiback_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihDaerah)

    def pilihDestinasinext_button_clicked(self):
        checked = self.pilihDestinasi.getCheckedVal()
        if (len(checked) == 0):
            # error dialog box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Destinasi Belum Dipilih!")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
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
        start_date, end_date = self.pilihTanggalPerjalanan.getDateSelected()
        if end_date is None:
            print(start_date)
        else:
            print(start_date, "to", end_date)
        self.widget.setCurrentWidget(self.home)