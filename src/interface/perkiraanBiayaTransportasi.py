import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class perkiraanBiayaTransportasiWindow(QDialog):
    def __init__(self):
        super(perkiraanBiayaTransportasiWindow, self).__init__()
        loadUi("src/interface/ui/perkiraanBiayaTransportasi.ui")