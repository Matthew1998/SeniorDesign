# This file defines the Object Dector classes and its sub-classes
import tensorflow as tf


class ObjectDetector(object):
    def __init__(self, model_path = ""):
        self.detectionGraph = self.loadModel(model_path + 'frozen_inference_graph.pb')
        self.prepareDetection()

    # loadModel - Goes to the described path and then loads the model found there
    #
    # @params:	path - path to graph
    #
    def loadModel(self, path):
        detectionGraph = tf.Graph()
        with detectionGraph.as_default():
            od_graph_def = tf.compat.v1.GraphDef()
            with tf.io.gfile.GFile(path, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        return detectionGraph

    # prepareDetection - Extracts the necessary infromation from the model found from loadModel
    # 					 and then stores them in local variables
    def prepareDetection(self):
        with self.detectionGraph.as_default():
            # Extract image tensor
            self.image_tensor = self.detectionGraph.get_tensor_by_name('image_tensor:0')
            # Extract detection boxes
            self.boxes = self.detectionGraph.get_tensor_by_name('detection_boxes:0')
            # Extract detection scores
            self.scores = self.detectionGraph.get_tensor_by_name('detection_scores:0')
            # Extract detection classes
            self.classes = self.detectionGraph.get_tensor_by_name('detection_classes:0')
            # Extract number of detections
            self.num_detections = self.detectionGraph.get_tensor_by_name('num_detections:0')


    # detectObject - This is the function that actually 
    def detectObject(self):
        with self.detectionGraph.as_default():
            with tf.compat.v1.Session(graph=self.detectionGraph) as sess:
                # Read frame
                image_np = cv2.imread(imgPath)
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image_np, axis=0)

                (self.boxes, self.scores, self.classes, self.num_detections) = sess.run(
                    [self.boxes, self.scores, self.classes, self.num_detections],
                    feed_dict={self.image_tensor: image_np_expanded})

    def getBoxes(self):
        return self.boxes

    def getScores(self):
        return self.scores

    def getClasses(self):
        return self.classes

    def getNumDetections(self):
        return self.num_detections

