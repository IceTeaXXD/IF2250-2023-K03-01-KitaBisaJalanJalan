import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class CatatanWindow(QDialog):
    def __init__(self):
        super(CatatanWindow, self).__init__()
        loadUi("./interface/ui/catatan.ui", self)

    def setDestinasi(self, destinasi):
        self.destinasi_box.setText(destinasi)