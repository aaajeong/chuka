import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
from moviepy.editor import *
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
import cv2
from utils import label_map_util
from utils import visualization_utils as vis_util

cap = cv2.VideoCapture('kleague_full.mp4')
video_for_cut = VideoFileClip('kleague_full.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
sys.path.append("..")

MODEL_NAME = 'soccer_highlight2'

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
            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8)
                
            if(int(cap.get(1)) % 5 == 0):

                title = "%d.jpg" % count
                count += 1
                cv2.imshow('object detection', cv2.resize(image_np, (800,600)))

                if (float(100 * scores[0][0]) > 99.7):
                    print(title)
                    hightlight.append(count)
                else:
                    if (count - 1 in hightlight and count + 1 not in hightlight):
                        cut.append(5*(count - 4))
                        print(count - 1)

                if (len(cut) > 1):
                    duration1 = cut[0] / fps
                    duration2 = cut[1] / fps
                    length = duration2 - duration1
                    print(length)
                    if (length > 60 or length <= 2):
                        cut[0] = cut[1]
                        del(cut[1])
                    else:
                        tmp_video = video_for_cut.subclip(duration1, duration2)
                        tmp_title = "%d.mp4" % cut_count
                        cut_count += 1
                        tmp_video.write_videofile(tmp_title, codec='libx264')
                        cut = []

            if cv2.waitKey(33) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break






