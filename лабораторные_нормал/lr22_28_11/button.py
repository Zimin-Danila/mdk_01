import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        button = QPushButton('Нажми меня!')
        # Переводим параметр Checkable нашей кнопки
        # в положение True - при нажатии кнопка будет
        # оставаться нажатой
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("Clicked!")
 # Эта функция уже принимает параметр checked, который
 # хранить состояние кнопки
    def the_button_was_toggled(self, checked):
        print("Кнопка зажата?", checked)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()