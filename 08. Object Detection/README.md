# **Computer Vision: Object Detection**

The [**Object Detection**](https://github.com/ThinamXx/ComputerVision/blob/main/08.%20Object%20Detection/ObjectDetection.ipynb) notebook contains implementation of object detection with PyTorch and pretrained networks. It also contains brief description about object detection and image preprocessing. 

📚**Notebook**
- [**Object Detection**](https://github.com/ThinamXx/ComputerVision/blob/main/08.%20Object%20Detection/ObjectDetection.ipynb)

**COCO Dataset**
- The [COCO Dataset](https://cocodataset.org/#home): Common Objects in Context, tends to be the standard for object detection benchmarking. The dataset contains over 90 classes of common objects we will see in everyday world.

**Object Detection**
- Object Detection is a computer technology related to computer vision and image processing that deals with detecting instances of semantic objects of a certain class. I will use PyTorch to perform object detection using the following state-of-the-art classification networks:
  - Faster R-CNN with a ResNet50.
  - Faster R-CNN with a MobileNet V3.
  - RetinaNet with a ResNet50.

**Image Preprocessing**
- Converting color channel ordering from BGR to RGB.
- Swapping color channel ordering from channels last to channels first.
- Adding a batch dimension.
- Scaling pixel intensities from the range [0, 255] to [0, 1].
- Converting the image from a numpy array to a floating point tensor.

![Image](https://github.com/ThinamXx/MachineLearning_DeepLearning/blob/main/Images/Day%2020a.PNG) 

![Image](https://github.com/ThinamXx/MachineLearning_DeepLearning/blob/main/Images/Day%2020b.PNG)
