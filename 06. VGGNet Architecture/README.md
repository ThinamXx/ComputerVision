# **Computer Vision: Mini VGGNet Architecture**

The [**Mini VGGNet**](https://github.com/ThinamXx/ComputerVision/blob/main/06.%20VGGNet%20Architecture/Mini%20VGGNet.ipynb) notebook contains the implementation of VGGNet Architecture. It makes the use of only *3 X 3* filters regardless of network depth. 

📚**Notebook**
- [**Mini VGGNet Architecture**](https://github.com/ThinamXx/ComputerVision/blob/main/06.%20VGGNet%20Architecture/Mini%20VGGNet.ipynb) 

**Logistic Regression**
- However, when unnecessary or excessive number of variables is used in logistic regression model, peculiarities i.e. special attributes of the underlying dataset disproportionately affect the coefficient of the model, the phenomena commonly known as overfitting. So, it is most important that the logistic regression model doesn't start training more variables than is justified for the given number of observations.

**Batch Normalization**
- Batch Normalization can lead to a faster, more stable convergence with higher accuracy. Batch Normalization will require more wall time to train the network even though the network will obtain higher accuracy in less epochs.

**VGGNet Architecture**
- I will define the build method of Mini VGGNet architecture below. It requires four parameters: width of input image, height of input image, depth of image, number of class labels in the classification task. The Sequential class, the building block of sequential networks sequentially stack one layer on top of the other layer initialized below. Batch Normalization operates over the channels, so in order to apply BN, we need to know which axis to normalize over.

![Image](https://github.com/ThinamXx/MachineLearning_DeepLearning/blob/main/Images/Day%2017.PNG)
