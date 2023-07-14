# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(372, 497)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.todoView = QListView(self.centralwidget)
        self.todoView.setObjectName(u"todoView")
        self.todoView.setGeometry(QRect(10, 20, 351, 241))
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(20, 410, 331, 31))
        self.todoEdit = QLineEdit(self.centralwidget)
        self.todoEdit.setObjectName(u"todoEdit")
        self.todoEdit.setGeometry(QRect(20, 370, 331, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 270, 331, 80))
        self.deleteButton = QPushButton(self.widget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(20, 30, 131, 24))
        self.completeButton = QPushButton(self.widget)
        self.completeButton.setObjectName(u"completeButton")
        self.completeButton.setGeometry(QRect(180, 30, 131, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 372, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\ub9ac\uc2a4\ud2b8 \ucd94\uac00", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.completeButton.setText(QCoreApplication.translate("MainWindow", u"\uc644\ub8cc", None))
    # retranslateUi

