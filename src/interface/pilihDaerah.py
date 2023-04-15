import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from classes import BoundaryDaerahWisata

class pilihDaerahWindow(QDialog):
    def __init__(self):
        super(pilihDaerahWindow, self).__init__()
        loadUi("./interface/ui/pilihDaerah.ui", self)
        daerahwisata = BoundaryDaerahWisata()
        for d in daerahwisata.getListDaerah():
            self.dropdown.addItem(d.getNama(), d.getID())