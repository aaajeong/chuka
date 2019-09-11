import sys
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
from moviepy.video.io.VideoFileClip import VideoFileClip
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
import cv2
from utils import label_map_util
from utils import visualization_utils as vis_util

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
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HighlightWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)

        self.setWindowTitle("Soccer Highlight")
        self.setWindowIcon(QIcon('./images/soccer.png'))
        self.setFixedWidth(640)
        self.setFixedHeight(480)
        # self.setStyleSheet("background-color: white")
        # self.setWindowOpacity()
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
        # layout.addItem(QSpacerItem(10, 200))

        # 파일 선택 버튼
        self.file_b = QPushButton('File Open')
        self.file_b.clicked.connect(self.pushButtonClicked)
        layout.addWidget(self.file_b, 1, 0)

        # 파일 이름 출력
        self.f_label = QLabel()
        layout.addWidget(self.f_label)

        # 리그 선택
        L_cb = QComboBox(self)
        L_cb.addItem('Laliga')
        L_cb.addItem('Serie A')
        L_cb.addItem('Ligue 1')
        L_cb.addItem('Bundesliga')
        L_cb.addItem('K-League')

        grp_2_layout.addLayout(layout)
        grp_2_layout.addWidget(L_cb)

        # 세 번째 그룹 QFormLaytout
        grp_3 = QGroupBox("Make HighLight")
        layout_base.addWidget(grp_3)
        layout = QFormLayout()
        grp_3.setLayout(layout)
        self.submit_b = QPushButton('확인')
        self.submit_b.clicked.connect(self.makeHighlight)
        layout.addRow(self.submit_b)



    # 파일 선택하는 함수
    def pushButtonClicked(self):
        fpath = QFileDialog.getOpenFileName(self)
        fname = fpath[0].split("/")[-1]
        self.f_label.setText(fname)
        return fname

    def makeHighlight(self):
        filename = self.f_label.text()
        cap = cv2.VideoCapture(filename)
        video_for_cut = VideoFileClip(filename)
        fps = cap.get(cv2.CAP_PROP_FPS)
        #sys.path.append("..")

        MODEL_NAME = 'soccer_highlight_goal2'

        # Path to frozen detection graph. This is the actual model that is used for the object detection.
        PATH_TO_FROZEN_GRAPH = MODEL_NAME + '/frozen_inference_graph.pb'

        # List of the strings that is used to add correct label for each box.
        PATH_TO_LABELS = os.path.join('training', 'object-detection.pbtxt')

        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.io.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

        def load_image_into_numpy_array(image):
            (im_width, im_height) = image.size
            return np.array(image.getdata()).reshape(
                (im_height, im_width, 3)).astype(np.uint8)

        count = 1
        cut_count = 0

        hightlight = []
        cut = []
        with detection_graph.as_default():
            with tf.compat.v1.Session(graph=detection_graph) as sess:
                while True:
                    ret, image_np = cap.read()
                    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                    image_np_expanded = np.expand_dims(image_np, axis=0)
                    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                    # Each box represents a part of the image where a particular object was detected.
                    boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                    # Each score represent how level of confidence for each of the objects.
                    # Score is shown on the result image, together with the class label.
                    scores = detection_graph.get_tensor_by_name('detection_scores:0')
                    classes = detection_graph.get_tensor_by_name('detection_classes:0')
                    num_detections = detection_graph.get_tensor_by_name('num_detections:0')
                    # Actual detection.

                    try:
                        (boxes, scores, classes, num_detections) = sess.run(
                            [boxes, scores, classes, num_detections],
                            feed_dict={image_tensor: image_np_expanded})
                    # 동영상 끝나면 highlightui로 넘어가게 된다.
                    except TypeError:
                        self.window = Ui_HighlightWindow()
                        self.window.show()

                        break

                    # Visualization of the results of a detection.
                    vis_util.visualize_boxes_and_labels_on_image_array(
                        image_np,
                        np.squeeze(boxes),
                        np.squeeze(classes).astype(np.int32),
                        np.squeeze(scores),
                        category_index,
                        use_normalized_coordinates=True,
                        line_thickness=8)

                    if (int(cap.get(1)) % 8 == 0):

                        title = "%d.jpg" % count
                        count += 1
                        # cv2.imshow('object detection', cv2.resize(image_np, (800, 600)))

                        if (float(100 * scores[0][0]) > 99.7):
                            print(title)
                            hightlight.append(count)
                        else:
                            if (count - 1 in hightlight and count + 1 not in hightlight):
                                cut.append(8 * (count - 4))
                                print(count - 1)

                        if (len(cut) > 1):
                            duration1 = cut[0] / fps
                            duration2 = cut[1] / fps
                            length = duration2 - duration1
                            print(length)
                            if (length > 60 or length <= 2):
                                cut[0] = cut[1]
                                del (cut[1])
                            else:
                                start_hour = (duration1 / 3600)
                                start_min = ((duration1 % 3600) / 60)
                                start_sec = duration1 % 60

                                end_hour = (duration2 / 3600)
                                end_min = ((duration2 % 3600) / 60)
                                end_sec = duration2 % 60

                                tmp_video = video_for_cut.subclip(duration1, duration2)
                                tmp_title = "./videos/%d+%d+%d~%d+%d+%d.mp4" % (
                                start_hour, start_min, start_sec, end_hour, end_min, end_sec)
                                cut_count += 1
                                tmp_video.write_videofile(tmp_title, codec='libx264')
                                cut = []


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyApp()
    form.show()
    exit(app.exec_())
