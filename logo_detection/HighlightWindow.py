# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HighlightWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#from SelectWindow import Ui_SelectWindow
#from Select import MyApp


class Ui_HighlightWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MyApp()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, HighlightWindow):
        HighlightWindow.setObjectName("HighlightWindow")
        HighlightWindow.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/soccer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HighlightWindow.setWindowIcon(icon)
        HighlightWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(HighlightWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(400, 10, 211, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow)        #HOME버튼 누르면 HOME 화면으로
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 611, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 220, 611, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 350, 611, 111))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(620, 10, 20, 451))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        HighlightWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HighlightWindow)
        self.statusbar.setObjectName("statusbar")
        HighlightWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HighlightWindow)
        QtCore.QMetaObject.connectSlotsByName(HighlightWindow)

    def retranslateUi(self, HighlightWindow):
        _translate = QtCore.QCoreApplication.translate
        HighlightWindow.setWindowTitle(_translate("HighlightWindow", "Soccer Highlight"))
        self.label.setText(_translate("HighlightWindow", "가져온 파일 명, 리그 "))
        self.pushButton.setText(_translate("HighlightWindow", "HOME"))
        self.label_2.setText(_translate("HighlightWindow", "영상, 시간 "))
        self.label_3.setText(_translate("HighlightWindow", "영상, 시간 "))
        self.label_4.setText(_translate("HighlightWindow", "영상, 시간 "))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HighlightWindow = QtWidgets.QMainWindow()
    ui = Ui_HighlightWindow()
    ui.setupUi(HighlightWindow)
    HighlightWindow.show()
    sys.exit(app.exec_())
