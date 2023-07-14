import sys

from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from MainWindow import Ui_MainWindow
from model import TodoModel


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("To Do List")
        self.model = TodoModel()
        self.todoView.setModel(self.model)
        self.addButton.pressed.connect(self.add)

        self.deleteButton.pressed.connect(self.delete)
        self.completeButton.pressed.connect(self.complete)

    def add(self):
        text = self.todoEdit.text()
        text = text.strip()

        if text:
            self.model.todos.append((False, text))

            # 트리거 리프레시 역할
            self.model.layoutChanged.emit()

            self.todoEdit.setText("")

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]

            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoView.clearSelection()

    def complete(self):
        indexes = self.todoView.selectedIndexes()

        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)

            self.model.dataChanged.emit(index, index)
            self.todoView.clearSelection()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec_()
