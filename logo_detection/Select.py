import sys
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from HighlightWindow import Ui_HighlightWindow

class MyApp(QWidget):

    def openWindow(self):
        self.window = Ui_HighlightWindow()
        self.window.show()

    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        self.setWindowTitle("Soccer Highlight")
        self.setWindowIcon(QIcon('./images/soccer.png'))
        self.setFixedWidth(640)
        self.setFixedHeight(480)
        #self.setStyleSheet("background-color: white")
        #self.setWindowOpacity()
        layout_base = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.setLayout(layout_base)

        # 첫 번째 그룹 QBoxLayout
        grp_1 = QGroupBox("LEAUGE")
        layout_base.addWidget(grp_1)
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("Laliga"))
        layout.addWidget(QPushButton("Serie A"))
        layout.addWidget(QPushButton("Ligue 1"))
        layout.addWidget(QPushButton("Bundesliga"))
        layout.addWidget(QPushButton("K-League"))
        grp_1.setLayout(layout)

        # 두 번째 그룹 QGridLayout
        grp_2 = QGroupBox("Select your file & League")
        layout_base.addWidget(grp_2)
        grp_2_layout = QBoxLayout(QBoxLayout.LeftToRight)
        grp_2.setLayout(grp_2_layout)
        layout = QGridLayout()
        #layout.addItem(QSpacerItem(10, 200))

        #파일 선택 버튼
        self.file_b = QPushButton('File Open')
        self.file_b.clicked.connect(self.pushButtonClicked)
        layout.addWidget(self.file_b, 1, 0)

        #파일 이름 출력
        self.f_label = QLabel()
        layout.addWidget(self.f_label)


        #리그 선택
        self.L_cb = QComboBox(self)
        # L_cb.addItem('Laliga')
        # L_cb.addItem('Serie A')
        # L_cb.addItem('Ligue 1')
        # L_cb.addItem('Bundesliga')
        # L_cb.addItem('K-League')
        self.L_cb.addItems(["Laliga", "Serie A", "Ligue 1", "Bundesliga", "K-League"])
        self.L_cb.currentTextChanged.connect(self.on_select)
        grp_2_layout.addLayout(layout)
        grp_2_layout.addWidget(self.L_cb)

        # 세 번째 그룹 QFormLaytout
        grp_3 = QGroupBox("Make HighLight")
        layout_base.addWidget(grp_3)
        layout = QFormLayout()
        grp_3.setLayout(layout)
        self.submit_b = QPushButton('확인')
        self.submit_b.clicked.connect(self.openWindow)       #파일 선택
        layout.addRow(self.submit_b)



    def pushButtonClicked(self):
        fpath = QFileDialog.getOpenFileName(self)
        fname = fpath[0].split("/")[-1]
        self.f_label.setText(fname)
        print(fname)
        f = open('file_league.txt','w')
        f.write(fname)
        f.close()

    def on_select(self):
        result2 = self.L_cb.currentText()
        f = open('file_league.txt', 'a')
        f.write(result2)
        f.close()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyApp()
    form.show()
    exit(app.exec_())