#@ IMPORTING LIBRARIES AND PACKAGES: 
import cv2
import numpy as np
import os

#@ INITIALIZING SIMPLE PREPROCESSOR:
class SimplePreprocessor:                                       # Defining Simple Preprocessor. 
    def __init__(self, width, height, inter=cv2.INTER_AREA):    # Initializing Constructor Function. 
        self.width = width                                      # Initialization. 
        self.height = height                                    # Initialization. 
        self.inter = inter                                      # Initialization. 

    def preprocess(self, image):                                # Defining Preprocess Function. 
        return cv2.resize(image, (self.width, self.height), 
                          interpolation=self.inter)             # Resizing Image.


#@ INITIALIZING DATASET LOADER: 
class SimpleDatasetLoader:                                      # Defining Simple Image Loader. 
    def __init__(self, preprocessors=None):                     # Initializing Constructor Function. 
        self.preprocessors = preprocessors                      # Initialization. 
        if self.preprocessors is None:                          # Inspection. 
            self.preprocessors = []                             # Initializing Empty List.
    
    def load(self, imagePaths, verbose=-1):                     # Defining Load Function. 
        data, labels = [], []                                   # Initializing Empty List.
        for (i, imagePath) in enumerate(imagePaths):
            image = cv2.imread(imagePath)                       # Reading Image. 
            label = imagePath.split(os.path.sep)[-2]            # Getting Labels. 
            if self.preprocessors is not None:
                for p in self.preprocessors:
                    image = p.preprocess(image)                 # Preprocessing Image. 
            data.append(image)                                  # Updating Data. 
            labels.append(label)                                # Updating Label. 
            if verbose > 0 and i > 0 and (i+1)%verbose == 0:
                print("[INFO] processed {}/{}".format(
                    i + 1, len(imagePaths)))                    # Showing Updates. 
        return (np.array(data), np.array(labels))               # Initializing Array of Data.

