import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

import home as home
import catatan as catatan
import pilihDaerah as pilihDaerah
import pilihDestinasi as pilihDestinasi
import image

class MainApplication(QApplication):
    def __init__(self, argv):
        super(MainApplication, self).__init__(argv)
        self.home = home.HomeWindow()
        self.catatan = catatan.CatatanWindow()
        self.pilihDaerah = pilihDaerah.pilihDaerahWindow()
        self.pilihDestinasi = pilihDestinasi.pilihDestinasiWindow()
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.home)
        self.widget.addWidget(self.catatan)
        self.widget.addWidget(self.pilihDaerah)
        self.widget.addWidget(self.pilihDestinasi)
        self.widget.setFixedWidth(1512)
        self.widget.setFixedHeight(982)
        self.widget.show()
        self.home.button_baru.clicked.connect(self.button_baru_clicked)
        self.pilihDaerah.back_button.clicked.connect(self.pilihDaerah_back_button_clicked)
        self.pilihDaerah.next_button.clicked.connect(self.pilihDaerah_next_button_clicked)
        self.pilihDestinasi.back_button.clicked.connect(self.pilihDestinasiback_button_clicked)
        self.catatan.back_button.clicked.connect(self.back_button_clicked)

    def button_baru_clicked(self):
        self.widget.setCurrentWidget(self.pilihDaerah)
    def pilihDaerah_next_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihDestinasi)
    def pilihDaerah_back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)
    def pilihDestinasiback_button_clicked(self):
        self.widget.setCurrentWidget(self.pilihDaerah)
    def back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)

run = MainApplication(sys.argv)
sys.exit(run.exec_())