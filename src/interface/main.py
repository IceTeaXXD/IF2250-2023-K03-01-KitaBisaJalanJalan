# GUI Main file
from home import*

app = QApplication(sys.argv)
window = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(1512)
widget.setFixedHeight(982)
widget.show()
sys.exit(app.exec_())