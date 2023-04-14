import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class PerkiraanBiayaTransportasiWindow(QDialog):
    def __init__(self):
        super(PerkiraanBiayaTransportasiWindow, self).__init__()
        loadUi("./interface/ui/perkiraanBiayaTransportasi.ui", self)
        self.show()