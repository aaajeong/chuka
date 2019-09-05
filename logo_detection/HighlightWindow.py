# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HighlightWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


import cv2
from PyQt5 import QtWidgets
import pygame
from moviepy.editor import *

#파일 경로 가져오기
path_dir = './video_test'

file_list = os.listdir(path_dir)        #path에 존재하는 파일 목록
file_list.sort()

"""
    파일 이름에서 특정 string을 가지는 파일만 뽑아내기
"""
# for item in file_list:
#     #some_string 이 파일 이름에 없을 경우 -1을 반환
#     if item.find('#')is not -1:
#         print(item)


class Ui_HighlightWindow(QWidget):


    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        # 배치될 위젯 변수 선언
        self.lb_1 = QLabel()
        self.centralWidget = QtWidgets.QWidget()
        self.s1 = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0,0,600,600))
        self.s1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.s1.setWidget(self.scrollAreaWidgetContents)


        #레이아웃 선언 및 HighlightWindow Widget에 설정
        self.layout_1 = QBoxLayout(QBoxLayout.TopToBottom, self)    #전체 레이아웃
        self.layout_2 = QBoxLayout(QBoxLayout.LeftToRight)          #파일 명 위한 레이아웃
        self.layout_3 = QBoxLayout(QBoxLayout.TopToBottom)          #파일버튼을 위한 레이아웃

        #부모레이아웃에 자식 레이아웃 추가
        self.layout_1.addLayout(self.layout_2)
        self.layout_1.addLayout(self.layout_3)


        self.setLayout(self.layout_1)
        self.init_widget()


    def init_widget(self):
        self.setWindowTitle("Soccer Highlight")
        self.setWindowIcon(QIcon('./images/soccer.png'))
        self.setFixedWidth(640)
        self.setFixedHeight(480)

        self.lb_1.setText('파일 명이 들어갈 자리')

        self.lb_1.setStyleSheet("background-color: yellow")




        self.layout_2.addWidget(self.lb_1)
        self.layout_3.addWidget(self.s1)
        self.layout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)


        #파일 리스트 버튼
        buttons = {}

        for item in file_list:
            buttons[item] = QtWidgets.QPushButton(str(item), self)
            buttons[item].clicked.connect(self.Button)
            self.layout_3.addWidget(buttons[item])


    def Button(self):
        sender = self.sender()
        print(sender.text())
        # 버튼 누르면 파일 재생
        filename = './video_test/' + sender.text()

        pygame.display.set_caption(sender.text())

        clip = VideoFileClip(filename)
        clip.preview()

        pygame.quit()





if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = Ui_HighlightWindow()
    form.show()
    exit(app.exec_())
