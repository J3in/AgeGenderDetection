import tensorflow as tf
import cv2 
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Dense, MaxPooling2D, Conv2D
from tensorflow.keras.layers import Input, Activation, Add
from tensorflow.keras.models import Model
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam,Adagrad,Adadelta,Adamax,RMSprop
import os

fldr="E:/age gender detection/UTkFace"
files=os.listdir(fldr)
ages=[]
images=[]
genders=[]

for fle in files:
    age=int(fle.split('_')[0])
    genders=str(fle.split('_')[1])
    total=fldr+'/'+fle
    print(total)
    image=cv2.imread(total)

    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image=cv2.resize(image,(48,48))
    images.append(image)
    age=int(fle.split('_')[0])
    gender=int(fle.split('_')[1])

plt.imshow(images[50])
print(ages[50])
print(genders[50])