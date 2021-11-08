import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
 
app = QtWidgets.QApplication([])
main = QtWidgets.QMainWindow()
main.resize(460, 275)
main.setWindowTitle('PyQt Hello World')
 
label = QtWidgets.QLabel("Hello World!")
label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
main.setCentralWidget(label)
 
font = QFont('Meiryo UI', 18, QFont.Light)
label.setFont(font)
 
main.show()
sys.exit(app.exec_())