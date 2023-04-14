import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class sedangBerlangsungWindow(QDialog):
    def __init__(self):
        super(sedangBerlangsungWindow, self).__init__()
        loadUi("./interface/ui/sedangBerlangsung2.ui", self)
        self.show()