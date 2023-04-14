import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

import home as home
import catatan as catatan

class MainApplication(QApplication):
    def __init__(self, argv):
        super(MainApplication, self).__init__(argv)
        self.home = home.HomeWindow()
        self.catatan = catatan.CatatanWindow()
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.home)
        self.widget.addWidget(self.catatan)
        self.widget.setFixedWidth(1512)
        self.widget.setFixedHeight(982)
        self.widget.show()
        self.home.button_baru.clicked.connect(self.button_baru_clicked)
        self.catatan.back_button.clicked.connect(self.back_button_clicked)

    def button_baru_clicked(self):
        self.widget.setCurrentWidget(self.catatan)

    def back_button_clicked(self):
        self.widget.setCurrentWidget(self.home)

run = MainApplication(sys.argv)
sys.exit(run.exec_())