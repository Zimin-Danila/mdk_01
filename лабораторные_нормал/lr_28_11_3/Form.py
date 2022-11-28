import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('C:\Programming\mdk_01\лабораторные_нормал\lr_28_11_\MyForm.ui')
window.show()
app.exec()
