import sys
import platform
import json

from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# GUI
from MainWindow import Ui_MainWindow
from model import TodoModel
from ui_splash_screen import Ui_SplashScreen

# GLOBAL
counter = 0
jumper = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("To Do List")
        self.model = TodoModel()
        self.load()
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
            self.save()

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]

            del self.model.todos[index.row()]
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
            with open("data.json", "r") as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open("data.json", "w") as f:
            data = json.dump(self.model.todos, f)


# ==> Splash screen window
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # --> 진행바 0 으로 초기화
        self.progressBarValue(0)

        # ---> 기본 타이틀 제거
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 제목 제거
        # 백그라운드 투명화
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # --> drop shadow effect 적용
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        # Qtimer --> 시작
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)

        # msec 타이머
        self.timer.start(10)

        # show ==> Main Window
        ########################################
        self.show()
        ## --> END ##

    # 로딩 함수
    ########################################
    def progress(self):
        global counter
        global jumper
        value = counter

        # html text 변경
        htmlText = """
        <p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>
        """

        # value 값 교체

        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if value > jumper:
            # new percentage text 적용
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10  # 10 단위로 증가

        # 진행 바 value 설정
        # fix max value error if > than 100 (디버깅 부분)
        if value >= 100:
            value = 1.000

        self.progressBarValue(value)

        # splash screen 종료와 to do list app 실행
        if counter > 100:
            self.timer.stop()

            # to do list app 실행
            self.main = MainWindow()
            self.main.show()

            # splash screen 종료
            self.close()

        counter += 0.5

    # 진행 바 value 함수
    ########################################

    def progressBarValue(self, value):

        # 진행 바 stylesheet
        stylesheet = """
        QFrame{
          border-radius: 150px;
          background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255))
        }
        """

        # value 값 얻기, float으로 변환하며 value로 전환
        # stop works of 1.000 to 0.000

        progress = (100 - value) / 100.0

        # get new values
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # set values to new stylesheet
        newStylesheet = stylesheet.replace(
            "{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # apply stylesheet with new values
        self.ui.circularProgress.setStyleSheet(newStylesheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = SplashScreen()
    app.exec_()
