import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class pilihDestinasiWindow(QDialog):
    def __init__(self):
        super(pilihDestinasiWindow, self).__init__()
        loadUi("./interface/ui/pilihDestinasi.ui", self)