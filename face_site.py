import cv2
import numpy as np
import os 

def Predict(imagePath) :

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainningdata.yml')
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    font = cv2.FONT_HERSHEY_SIMPLEX

    #iniciate id counter
    id = 0

    # names related to ids: 
    names = ['None', 'Archi', 'Shruti', 'Rohit'] 
    img = cv2.imread(imagePath)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
        )

    for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less than 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            # cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            # cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    return id
    