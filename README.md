# RoadAware Application

**KAGGLE-DATASET:**
This repository consists of dataset downloaded from Kaggle. Due to its large size, only a small portion of the training dataset has been uploaded.
Link to the Kaggle dataset: https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign

**TRS.py:**

This file contains the code to the backend of RoadAware. The Machine Learning model used for RoadAware is trained using a Neural Network. The model was initially trained in 15 epochs and the results are shown in the following files:
  1. RoadAware-epochs: This graph shows the variation of accuracy of the Neural Network as the number of epochs increase
  2. RoadAware-training-loss: This graph shows the variation of loss of the Neural Network as the number of epochs increase
  3. RoadAware-training-output and RoadAware-training-output2: The data for the above two has been collected during the training of the Neural Network. These two images show the training of the Neural Network. 

From the above information, epochs = 10 seems to be a good number.

**RoadAware_ML_model.h5:**

The final trained ML model.

**Accuracy_TSR.py:**

This file contains the code to test the accuracy of the Machine Learning model in RoadAware_ML_model.h5. The accuracy on the model using the test data is 0.935. 

**TSR_GUI.py:**

This file contains the GUI for RoadAware application


**TO RUN:**



python 3.8 is required.

Please ensure the following packages are installed

numpy

kivy

opencv2

The following files should be downloaded:

TSR_GUI.py

RoadAware_ML_model.h5

In terminal type

>>>python

Followed by:

>>>python TSR_GUI.py


