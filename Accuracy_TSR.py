import pandas as pd 
from PIL import Image
import numpy as np 
from keras.models import load_model
#testing accuracy on test dataset
from sklearn.metrics import accuracy_score
#load the ML model
model = load_model('RoadAware_ML_model.h5')
#read the test dataset
y_test = pd.read_csv('Test.csv')
labels = y_test["ClassId"].values
imgs = y_test["Path"].values
data=[]
for img in imgs:
    image = Image.open(img)
    image = image.resize((30,30))
    data.append(np.array(image))
X_test=np.array(data)
#predict on the test images
pred = np.argmax(model.predict(X_test),axis = -1)
#Accuracy with the test data
print(accuracy_score(labels, pred))
