import cv2

#pretrained algorithm 
classifier_file = 'cars.xml'

#create classifier 
car_tracker = cv2.CascadeClassifier(classifier_file)

#capture video
video = cv2.VideoCapture('Tesla FSD Autopilot Dashcam Compilation.mp4')

while True:
    #Read  the current frame 
    (read_successful, frame) = video.read()

    if read_successful:
        #convert to black and white (grey scale)
        grey_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    #detect cars 
    cars = car_tracker.detectMultiScale(grey_scale)
    

    #Draw the rectangle around the cars 
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y),((x+w), (y+h)), (0, 255, 0), 3)

    #Show the image with the cars spotted
    cv2.imshow('My car detection app', frame)

    #to avoid immediate close, close only on key press 
    cv2.waitKey(1)

cv2.waitKey(1)
















