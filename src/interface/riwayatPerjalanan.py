import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class riwayatPerjalananWindow(QDialog):
    def __init__(self):
        super(riwayatPerjalananWindow, self).__init__()
        loadUi("./interface/ui/riwayatPerjalanan.ui", self)
        self.show()