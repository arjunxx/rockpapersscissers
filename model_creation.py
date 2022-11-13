import os
import cv2
import numpy as np
import keras
#defining the folders into variables
main_folder = 'images'
subfolders= ['paper','rock','scissors']

#creating data and labels
data = []
labels = []

#loop goes through each individual subfolder one by one
for folder_name in subfolders:
    folder_path = os.path.join(main_folder,folder_name)
    folder_images = os.listdir(folder_path)

    #goes through each image in each subfolder
    for each_image in folder_images:
        image_path = os.path.join(folder_path, each_image)

        #set's image (resizing, recoloring, etc.)
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        okay, bw = cv2.threshold(gray_image, 130, 255, cv2.THRESH_BINARY_INV)
        resized_image = cv2.resize(bw, (50,50))

        #adding newly made image to the data list
        data.append(resized_image)
        if folder_name == 'paper':
            labels.append(0)
        if folder_name == 'rock':
            labels.append(1)
        if folder_name == 'scissors':
            labels.append(2)

#converting data and labels list into an array
data = np.array(data)
print(data.shape)
labels = np.array(labels)

#creating model using keras

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(50,50)),
    keras.layers.Dense(512, activation = 'relu'), #relu get's rid of nodes with less than 50% accuracy
    keras.layers.Dense(3, activation = 'softmax')]) #gives accuracy in the form of a number between 0-1

model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics= ['accuracy'])
#displays accuracy and loss
model.fit(data, labels, epochs=50)
model.save('rockps.h5')


