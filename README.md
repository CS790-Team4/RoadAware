# RoadAware Application

KAGGLE-DATASET:
This repository consists of dataset downloaded from Kaggle. Due to its large size, only a small portion of the training dataset has been uploaded.
Link to the Kaggle dataset: https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign

TRS.py:
This file contains the code to the backend of RoadAware. The Machine Learning model used for RoadAware is trained using a Neural Network. The model was initially trained in 15 epochs and the results are shown in the following files:
  1. RoadAware-epochs: This graph shows the variation of accuracy of the Neural Network as the number of epochs increase
  2. RoadAware-training-loss: This graph shows the variation of loss of the Neural Network as the number of epochs increase
  3. RoadAware-training-output and RoadAware-training-output2: The data for the above two has been collected during the training of the Neural Network. These two images show the training of the Neural Network. 

From the above information, epochs = 10 seems to be a good number.

RoadAware_ML_model.h5:
The final trained ML model.
