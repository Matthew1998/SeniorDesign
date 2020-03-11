# This file will be using the TensorFlow model in the following directory
#     /home/seniordesign/TensorFlow/CompletedModels/lugnut

import turtle
import time
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import cv2

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

MODEL_PATH = '/home/pi/Desktop/SeniorDesign/TempFiles/'
IMAGE_PATH = '/home/pi/Desktop/SeniorDesign/TempFiles/images/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
CKPT_PATH = '/home/pi/Desktop/SeniorDesign/Models/bolt_rev1_frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
LABEL_PATH = MODEL_PATH + 'data/label_map.pbtxt'

# Number of classes to detect
NUM_CLASSES = 1

wn = turtle.Screen()
wn.screensize(800, 600)
todd = turtle.Turtle()
todd.shape('turtle')
todd.penup()


# Load a (frozen) Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(CKPT_PATH, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')


# Loading label map
#     Label maps map indices to category names, so that when our convolution network predicts `5`
#     we know that this corresponds to `airplane`.  Here we use internal utility functions,
#     but anything that returns a dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(LABEL_PATH)
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


# Helper code
def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)

#Display results with turtle graphics
def useTurtle(boxes, scores):
    wn.clear()

    scores = scores.tolist()[0]
    boltList = []
    for i in range(len(scores)):
        if scores[i] > 0.5:
            boltList.append(boxes[0][i])

    boxPointList = []

    # Boxes are the following [ y_min , x_min , y_max , x_max ]
    for box in boltList:
        minY = box[0]*400
        minX = box[1]*400
        maxY = box[2]*400
        maxX = box[3]*400
        coordinate = [(minX, minY), (minX, maxY), (maxX, maxY), (maxX, minY)]
        boxPointList.append(coordinate)

    avgPointList = []

    for box in boltList:
        avgY = ((box[0]*400) + (box[2]*400))/2
        avgX = ((box[1]*400) + (box[3]*400))/2
        coordinate = (avgX, avgY)
        avgPointList.append(coordinate)

    for point in avgPointList:
        todd.dot()
        todd.goto(point[0], point[1])
        todd.dot()


    for box in boxPointList:
        for corner in box:
            todd.goto(corner[0], corner[1])
            todd.dot()



# Detection
iterator = 0
#tens = 0
with detection_graph.as_default():
    with tf.compat.v1.Session(graph=detection_graph) as sess:
        while True:
            print("Began Process")
            iterator += 1
            #ones = iterator%10
            #tens = iterator//10
            # Read frame from camera
            image_np = cv2.imread('/home/pi/Desktop/SeniorDesign/TempFiles/images/' + str(iterator) + '.jpg')
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            # Extract image tensor
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Extract detection boxes
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Extract detection scores
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            # Extract detection classes
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            # Extract number of detectionsd
            num_detections = detection_graph.get_tensor_by_name(
                'num_detections:0')
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
                line_thickness=1)

            # Display output
            cv2.imshow('object detection', cv2.resize(image_np, (800, 600)))
#            useTurtle(boxes, scores)
#            input()
            cv2.waitKey(0)

