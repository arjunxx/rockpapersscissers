import cv2


#creates the data sets for each of the 3 files "ROCK" "PAPER" "SCISSORS" 


#set's the video camera size
camera = cv2.VideoCapture(0)
camera.set(3,640)
camera.set(4,480)
x1 = 320
y1 = 0
x2 = 640
y2 = 240
flag = 0
count = 0
roi = 0
#starts loop to run video
while True :
    ret,video = camera.read()
    video = cv2.flip(video,1)
    #changing video to black and white
    gray_video = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    okay, bw = cv2.threshold(gray_video, 130, 255, cv2.THRESH_BINARY_INV)

    #takes a 100 screen shots (1 ss per second)
    if flag == 1:
        cv2.imwrite("images/paper/screenshot"+str(count)+".png", roi)
        count += 1
        print(count)
    if count == 100:
        flag = 0
        break
        
    if ret == True:
        cv2.rectangle(video, (x1,y1), (x2,y2), (0,190,0), 2)
        roi = bw[y1:y2, x1:x2]
        
        cv2.imshow("video 1", roi)

        if cv2.waitKey(60) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(60) &0xFF == ord('s'):
            #cv2.imwrite("screenshot.png", roi)
            print('s')
            flag = 1

        
camera.release()
cv2.destroyAllWindows()
