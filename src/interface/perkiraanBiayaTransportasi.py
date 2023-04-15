import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

# from classes import ListTransportasi
import image


arrray_of_destiansi = [['Destinasi 1',10000,20000,30000,40000],['Destinasi 2',16000,20000,30000,40000],['Destinasi 3',10090,20000,30000,40000]]
class PerkiraanBiayaTransportasiWindow(QDialog):
    def __init__(self):
        super(PerkiraanBiayaTransportasiWindow, self).__init__()
        loadUi("./interface/ui/perkiraanBiayaTransportasi.ui", self)

        # listTransport = ListTransportasi()

        # # Menampilkan harga per transportasi
        # for t in listTransport.getList():
        #     if t.getNama() == "Kereta":
        #         # Kasih Harganya
        #         self.harga_kereta.setText(str(t.getHarga()))
        #     elif (t.getNama() == "Mobil"):
        #         # Kasih Harganya
        #         self.harga_mobil.setText(str(t.getHarga()))
        #     elif (t.getNama() == "Pesawat"):
        #         # Kasih Harganya
        #         self.harga_pesawat.setText(str(t.getHarga()))
        #     else:
        #         # Kasih Harganya
        #         self.harga_bus.setText(str(t.getHarga()))
        # Nanti buat tiap object radioButton
        # dicek is set or not
        # kalo is set, pass ID via getID()
        # make a scroll area
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, 250, 100, 300)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)
        self.setLayout(self.verticalLayout)
        
        for i in range(len(arrray_of_destiansi)):
            self.container = QLabel()
            self.container.setFixedSize(1200, 400)
            self.container.setStyleSheet("background-color: transparent; border-radius: 10px; margin-bottom : 20px")

            box = QHBoxLayout(self.container)
            box.setContentsMargins(0, 0, 0, 0)
            box.setSpacing(40)

            # box di kiri
            left_box = QLabel()
            left_box.setFixedSize(400, 400)
            left_box.setStyleSheet("background-color: #F2F2F2; border-radius: 10px;")

            decoration = QLabel()
            decoration.setFixedSize(400, 40)
            decoration.setStyleSheet("background-color: #03EF62; border-radius: 10px;")

            title = QLabel(arrray_of_destiansi[i][0])
            title.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold;")

            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)
            line.setStyleSheet("background-color: #000000; margin:10; padding: 0;")
            line.setFixedSize(380, 1)

            desc = QLabel("lorem ipsum dolor sir amet")
            desc.setStyleSheet("color: #000000; font-size: 16px;")
            desc.setWordWrap(True)
            desc.setContentsMargins(10, 0, 0, 0)


            left_box_layout = QVBoxLayout(left_box)
            left_box_layout.addWidget(decoration)
            left_box_layout.addWidget(title)
            left_box_layout.addWidget(line)
            left_box_layout.addWidget(desc)
            left_box_layout.setContentsMargins(0, 0, 0, 0)

            box.addWidget(left_box)
            decoration.setAlignment(Qt.AlignTop)
            title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            line.setContentsMargins(0, 0, 0, 0)
            desc.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    
            decoration.setMargin(0)
            right_box = QLabel()
            right_box.setFixedSize(800, 400)
            right_box.setStyleSheet("background-color: #F2F2F2; border-radius: 10px;")
            right_box_layout = QVBoxLayout(right_box)
            right_box_layout.setContentsMargins(0, 0, 0, 0)
            # right_box.setAlignment(Qt.AlignCenter)

            tiket_kereta = QLabel()
            tiket_kereta.setContentsMargins(0, 0, 0, 0)
            tiket_kereta.setMaximumWidth(600)
            tiket_kereta.setMaximumHeight(200)

            label_kereta = QLabel("Tiket Kereta Rp. " + str(arrray_of_destiansi[i][1]))
            label_kereta.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold; margin-bottom : 20px; margin-top : 20px; ")
            # set coordinate
            label_kereta.setContentsMargins(0, 0, 0, 0)
            
            # add an image
            img_kereta = QLabel()
            img_kereta.setStyleSheet("background-color: #000000; border-radius: 10px; margin-bottom : 20px")
            img_kereta.setPixmap(QPixmap("D:/Semester IV/RPL/2/if2250-2023-k03-01-kitabisajalanjalan/img/biayaTransport/Train.png"))
            img_kereta.setStyleSheet("background-color : transparent;")
            img_kereta.setMaximumWidth(50)
            # img_kereta.setMaximumHeight(100)

            # define a button group
            group = QButtonGroup()
            # make a radio button
            radio_kereta = QRadioButton()
            group.addButton(radio_kereta)
            radio_kereta.setStyleSheet("background-color : transparent; margin-top: 20px; margin-left : 20px")

            # add to layout
            layout_kereta = QHBoxLayout(tiket_kereta)
            layout_kereta.setContentsMargins(0, 0, 0, 0)
            layout_kereta.addWidget(radio_kereta)
            layout_kereta.addWidget(img_kereta)
            layout_kereta.addWidget(label_kereta)
            layout_kereta.setAlignment(Qt.AlignCenter)


            tiket_mobil = QLabel()
            tiket_mobil.setContentsMargins(0, 0, 0, 0)
            tiket_mobil.setMaximumWidth(600)
            tiket_mobil.setMaximumHeight(200)

            label_mobil = QLabel("Tiket Mobil Rp. " + str(arrray_of_destiansi[i][2]))
            label_mobil.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold; margin-bottom : 20px; margin-top : 20px; ")
            # set coordinate
            label_mobil.setContentsMargins(0, 0, 0, 0)

            # add an image
            img_mobil = QLabel()
            img_mobil.setStyleSheet("background-color: #000000; border-radius: 10px; margin-bottom : 20px")
            img_mobil.setPixmap(QPixmap("D:/Semester IV/RPL/2/if2250-2023-k03-01-kitabisajalanjalan/img/biayaTransport/People in Car.png"))
            img_mobil.setStyleSheet("background-color : transparent;")
            img_mobil.setMaximumWidth(70)

            # make a radio button
            radio_mobil = QRadioButton()
            group.addButton(radio_mobil)
            radio_mobil.setStyleSheet("background-color : transparent; margin-top: 20px; margin-left : 20px")

            # add to layout
            layout_mobil = QHBoxLayout(tiket_mobil)
            layout_mobil.setContentsMargins(0, 0, 0, 0)
            layout_mobil.addWidget(radio_mobil)
            layout_mobil.addWidget(img_mobil)
            layout_mobil.addWidget(label_mobil)
            layout_mobil.setAlignment(Qt.AlignCenter)

            tiket_pesawat = QLabel()
            tiket_pesawat.setContentsMargins(0, 0, 0, 0)
            tiket_pesawat.setMaximumWidth(600)
            tiket_pesawat.setMaximumHeight(200)

            label_pesawat = QLabel("Tiket Pesawat Rp. " + str(arrray_of_destiansi[i][3]))
            label_pesawat.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold; margin-bottom : 20px; margin-top : 20px; ")
            # set coordinate
            label_pesawat.setContentsMargins(0, 0, 0, 0)

            # add an image
            img_pesawat = QLabel()
            img_pesawat.setStyleSheet("background-color: #000000; border-radius: 10px; margin-bottom : 20px")
            img_pesawat.setPixmap(QPixmap("D:/Semester IV/RPL/2/if2250-2023-k03-01-kitabisajalanjalan/img/biayaTransport/Plane.png"))
            img_pesawat.setStyleSheet("background-color : transparent;")
            img_pesawat.setMaximumWidth(70)

            # make a radio button
            radio_pesawat = QRadioButton()
            group.addButton(radio_pesawat)
            radio_pesawat.setStyleSheet("background-color : transparent; margin-top: 20px; margin-left : 58px")

            # add to layout
            layout_pesawat = QHBoxLayout(tiket_pesawat)
            layout_pesawat.setContentsMargins(0, 0, 0, 0)
            layout_pesawat.addWidget(radio_pesawat)
            layout_pesawat.addWidget(img_pesawat)
            layout_pesawat.addWidget(label_pesawat)
            layout_pesawat.setAlignment(Qt.AlignCenter)

            tiket_bus = QLabel()
            # tiket_bus.setMargin(-100)
            tiket_bus.setContentsMargins(0, 0, 0, 0)
            tiket_bus.setMaximumWidth(620)
            tiket_bus.setMaximumHeight(200)

            label_bus = QLabel("Tiket Bus Rp. " + str(arrray_of_destiansi[i][4]))
            label_bus.setStyleSheet("color: #000000; font-size: 32px; font-weight: bold; margin-bottom : 20px; margin-top : 20px; ")
            # set coordinate
            label_bus.setContentsMargins(0, 0, 0, 0)

            # add an image
            img_bus = QLabel()
            img_bus.setStyleSheet("background-color: #000000; border-radius: 10px; margin-bottom : 20px")
            img_bus.setPixmap(QPixmap("D:/Semester IV/RPL/2/if2250-2023-k03-01-kitabisajalanjalan/img/biayaTransport/Bus.png"))
            img_bus.setStyleSheet("background-color : transparent;")
            img_bus.setMaximumWidth(120)

            # make a radio button
            radio_bus = QRadioButton()
            group.addButton(radio_bus)
            radio_bus.setStyleSheet("background-color : transparent; margin-top: 20px;")

            # add to layout
            layout_bus = QHBoxLayout(tiket_bus)
            layout_bus.setContentsMargins(0, 0, 0, 0)
            layout_bus.addWidget(radio_bus)
            layout_bus.addWidget(img_bus)
            layout_bus.addWidget(label_bus)
            layout_bus.setAlignment(Qt.AlignCenter)

            right_box_layout.addWidget(tiket_kereta)
            right_box_layout.addWidget(tiket_mobil)
            right_box_layout.addWidget(tiket_pesawat)
            right_box_layout.addWidget(tiket_bus)
            right_box_layout.setContentsMargins(0, 0, 0, 0)
            # img_kereta.move(0, 0)

            # right_box.setText("Harga Tiket Kereta : "+str(arrray_of_destiansi[i][1])+"\nHarga Tiket Mobil : "+str(arrray_of_destiansi[i][2])+"\nHarga Tiket Pesawat : "+str(arrray_of_destiansi[i][3])+"\nHarga Tiket Bus : "+str(arrray_of_destiansi[i][4]))
            box.addWidget(right_box)

            self.gridLayout.addWidget(self.container, i, 0, 1, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PerkiraanBiayaTransportasiWindow()
    window.show()
    sys.exit(app.exec_())