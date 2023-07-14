from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt

tick = QtGui.QImage('img/tick.png')


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        # self.todos는 [(bool,str),(bool,str)] 구조의 변수.
        # "todos or []" 는 인자 todos가 있다면(true)
        # @todos를 저장하고 없다면(false), list([]) 저장

        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            # status가 true일때 즉, 완료버튼을 눌렀을때 tick 이미지 리턴
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)
