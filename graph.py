# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
        MainWindow.resize(460, 388)
        MainWindow.setMaximumSize(QSize(460, 388))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Button_8 = QPushButton(self.centralwidget)
        self.Button_8.setObjectName(u"Button_8")
        self.Button_8.setGeometry(QRect(100, 130, 81, 51))
        font = QFont()
        font.setFamily(u"Microsoft YaHei")
        font.setPointSize(18)
        self.Button_8.setFont(font)
        self.Button_9 = QPushButton(self.centralwidget)
        self.Button_9.setObjectName(u"Button_9")
        self.Button_9.setGeometry(QRect(190, 130, 81, 51))
        self.Button_9.setFont(font)
        self.Button_7 = QPushButton(self.centralwidget)
        self.Button_7.setObjectName(u"Button_7")
        self.Button_7.setGeometry(QRect(10, 130, 81, 51))
        self.Button_7.setFont(font)
        self.Button_multiply = QPushButton(self.centralwidget)
        self.Button_multiply.setObjectName(u"Button_multiply")
        self.Button_multiply.setGeometry(QRect(280, 130, 81, 51))
        self.Button_multiply.setFont(font)
        self.Button_6 = QPushButton(self.centralwidget)
        self.Button_6.setObjectName(u"Button_6")
        self.Button_6.setGeometry(QRect(190, 190, 81, 51))
        self.Button_6.setFont(font)
        self.Button_4 = QPushButton(self.centralwidget)
        self.Button_4.setObjectName(u"Button_4")
        self.Button_4.setGeometry(QRect(10, 190, 81, 51))
        self.Button_4.setFont(font)
        self.Button_minus = QPushButton(self.centralwidget)
        self.Button_minus.setObjectName(u"Button_minus")
        self.Button_minus.setGeometry(QRect(280, 190, 81, 51))
        self.Button_minus.setFont(font)
        self.Button_5 = QPushButton(self.centralwidget)
        self.Button_5.setObjectName(u"Button_5")
        self.Button_5.setGeometry(QRect(100, 190, 81, 51))
        self.Button_5.setFont(font)
        self.Button_3 = QPushButton(self.centralwidget)
        self.Button_3.setObjectName(u"Button_3")
        self.Button_3.setGeometry(QRect(190, 250, 81, 51))
        self.Button_3.setFont(font)
        self.Button_1 = QPushButton(self.centralwidget)
        self.Button_1.setObjectName(u"Button_1")
        self.Button_1.setGeometry(QRect(10, 250, 81, 51))
        self.Button_1.setFont(font)
        self.Button_and = QPushButton(self.centralwidget)
        self.Button_and.setObjectName(u"Button_and")
        self.Button_and.setGeometry(QRect(280, 250, 81, 51))
        self.Button_and.setFont(font)
        self.Button_2 = QPushButton(self.centralwidget)
        self.Button_2.setObjectName(u"Button_2")
        self.Button_2.setGeometry(QRect(100, 250, 81, 51))
        self.Button_2.setFont(font)
        self.Button_point = QPushButton(self.centralwidget)
        self.Button_point.setObjectName(u"Button_point")
        self.Button_point.setGeometry(QRect(100, 310, 81, 51))
        self.Button_point.setFont(font)
        self.Button_OK = QPushButton(self.centralwidget)
        self.Button_OK.setObjectName(u"Button_OK")
        self.Button_OK.setGeometry(QRect(190, 310, 171, 51))
        self.Button_OK.setFont(font)
        self.Button_0 = QPushButton(self.centralwidget)
        self.Button_0.setObjectName(u"Button_0")
        self.Button_0.setGeometry(QRect(10, 310, 81, 51))
        self.Button_0.setFont(font)
        self.Button_up = QPushButton(self.centralwidget)
        self.Button_up.setObjectName(u"Button_up")
        self.Button_up.setGeometry(QRect(190, 70, 81, 51))
        self.Button_up.setFont(font)
        self.Button_left = QPushButton(self.centralwidget)
        self.Button_left.setObjectName(u"Button_left")
        self.Button_left.setGeometry(QRect(10, 70, 81, 51))
        self.Button_left.setFont(font)
        self.Button_divide = QPushButton(self.centralwidget)
        self.Button_divide.setObjectName(u"Button_divide")
        self.Button_divide.setGeometry(QRect(280, 70, 81, 51))
        self.Button_divide.setFont(font)
        self.Button_right = QPushButton(self.centralwidget)
        self.Button_right.setObjectName(u"Button_right")
        self.Button_right.setGeometry(QRect(100, 70, 81, 51))
        self.Button_right.setFont(font)
        self.Button_ce = QPushButton(self.centralwidget)
        self.Button_ce.setObjectName(u"Button_ce")
        self.Button_ce.setGeometry(QRect(370, 190, 81, 171))
        self.Button_ce.setFont(font)
        self.Button_del = QPushButton(self.centralwidget)
        self.Button_del.setObjectName(u"Button_del")
        self.Button_del.setGeometry(QRect(370, 70, 81, 111))
        self.Button_del.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 11, 441, 51))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(18)
        self.lineEdit.setFont(font1)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u79d1\u5b66\u8ba1\u7b97\u5668", None))
        self.Button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Button_multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.Button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Button_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Button_and.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.Button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Button_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.Button_OK.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_up.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.Button_left.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.Button_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.Button_right.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.Button_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.Button_del.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
    # retranslateUi
