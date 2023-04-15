import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class pilihTanggalPerjalananWindow(QDialog):
    def __init__(self):
        super(pilihTanggalPerjalananWindow, self).__init__()
        loadUi("./interface/ui/pilihTanggalPerjalanan.ui", self)