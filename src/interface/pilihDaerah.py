import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class pilihDaerahWindow(QDialog):
    def __init__(self):
        super(pilihDaerahWindow, self).__init__()
        loadUi("src/interface/ui/pilihDaerah.ui", self)
        self.show()