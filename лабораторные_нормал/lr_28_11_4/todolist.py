import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

Ui_MainWindow, QtBaseClass = uic.loadUiType('C:\Programming\mdk_01\лабораторные_нормал\lr_28_11\MyTodo.ui')
tick = QtGui.QImage('C:\Programming\mdk_01\лабораторные_нормал\lr_28_11\\tick.png')
class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []
    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text
        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick
    def rowCount(self, index):
        return len(self.todos)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model = TodoModel()
        self.todoView.setModel(self.model)
        self.load()
 # Подключаем кнопку
        self.addButton.pressed.connect(self.add)
        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)
    def add(self):
 # Забираем значение из текстового поля
        text = self.todoEdit.text()
        if text:
 # Дополняем наш список
            self.model.todos.append((False, text))
            print(self.model.todos)
            self.model.layoutChanged.emit()
 # Очищаем
            self.todoEdit.setText('')
            self.save()
    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
 # indexes - это список одиночных элементов
            index = indexes[0]
            del self.model.todos[index.row()]
 # print(self.model.todos)
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()
            self.save()
    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()
            self.save()
    def load(self):
        try:
            with open('data.json', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass
    def save(self):
        with open('data.json', 'w') as f:
            data = json.dump(self.model.todos, f)
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()