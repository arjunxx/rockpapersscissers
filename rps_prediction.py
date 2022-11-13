import cv2
import numpy as np
from keras.models import load_model
model = load_model('rockps.h5')
#set's the video camera size
camera = cv2.VideoCapture(0)
camera.set(3,640)
camera.set(4,480)
x1 = 320
y1 = 0
x2 = 640
y2 = 240
roi = 0
things = ['paper','rock', 'scissors']
#starts loop to run video
while True :
    ret,video = camera.read()
    video = cv2.flip(video,1)
    #changing video to black and white
    gray_video = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    okay, bw = cv2.threshold(gray_video, 130, 255, cv2.THRESH_BINARY_INV)

    if ret == True:
        cv2.rectangle(video, (x1,y1), (x2,y2), (0,190,0), 2)
        roi = bw[y1:y2, x1:x2]
        resized_roi = cv2.resize(roi, (50,50))
        reshaped_roi = np.reshape(resized_roi, (1,50,50))
        p= model.predict(reshaped_roi)
        p = p[0]
        highest_index = np.argmax(p)
        print(things[highest_index])
        cv2.imshow("video 1", roi)

        if cv2.waitKey(60) & 0xFF == ord('q'):
            break

        
camera.release()
cv2.destroyAllWindows()
