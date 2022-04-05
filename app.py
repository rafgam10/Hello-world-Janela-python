from cProfile import label
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
okButton = QPushButton('OK')
cancelButton = QPushButton('Cancel')
label = QLabel('Olá tudo bom? Hello world!!!')
label.setFont(QFont('Ariel', 20))
hbox = QHBoxLayout()

hbox.addStretch(1)
hbox.addWidget(okButton)
hbox.addWidget(cancelButton)
vbox = QVBoxLayout()
vbox.addStretch(1)
vbox.addWidget(label)
vbox.addLayout(hbox)
win = QWidget()
win.setLayout(vbox)

win.setWindowTitle("Teste da Janela")
win.show()
sys.exit(app.exec_())