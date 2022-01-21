# **Computer Vision: Pretrained Convolutional Neural Networks**

- The [**Pretrained CNNs**](https://github.com/ThinamXx/ComputerVision/blob/main/07.%20Pretrained%20CNNs/PretrainedCNNs.ipynb) notebook contains the reviews of convolutional neural networks and implementation of VGG16 and Xception networks for classification of images.

📚**Notebook:**
- [**Pretrained CNNs**](https://github.com/ThinamXx/ComputerVision/blob/main/07.%20Pretrained%20CNNs/PretrainedCNNs.ipynb) 

**Convolutional Neural Networks:**
- Convolutions are just a type of matrix multiplication with two constraints on the weight matrix: some elements are always zero and some elements are tied or forced to always have the same value. Batch Normalization adds some extra randomness to the training process. Larger batches have gradients that are more accurate since they are calculated from more data. But larger batch size means fewer batches per epoch which means fewer opportunities for the model to update weights. VGG16, VGG19, and ResNet all accept 224 x 224 input images while InceptionV3 and Xception requires 299 x 299 pixel inputs.

![Image](https://github.com/ThinamXx/MachineLearning_DeepLearning/blob/main/Images/Day%2019.PNG)

