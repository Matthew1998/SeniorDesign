from getImage.py import Image
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

flags = tf.app.flags
flags.DEFINE_string('image_directory','', 'Path to images')
flags.DEFINE_string('model_path', '', 'Path to the model being used')
flags.DEFINE_string('label_path', '', 'Path to the label map')


FLAGS = flags.FLAGS

