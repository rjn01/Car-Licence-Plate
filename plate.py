import cv2
import numpy as np
import os

haarcascade_plate = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")   	##using haarcascade classifier
cap = cv2.VideoCapture(0)  								#opening webcam, we can also give the path of video
number = 0
while True:
	_,frame = cap.read()
	
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  				#converting coloured frame to gray
	
	plate = haarcascade_plate.detectMultiScale(gray_frame,1.3,5)			#detecting number plates
	
	for (x,y,w,h) in plate:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 			#rectangle around the plate in the frame
		roi = gray_frame[y:y+h,x:x+w]						#selecting  region of interest
		cv2.imshow("roi",roi)

		image_name = str(number) +".jpg"
		
		path = os.path.join(r"C:\Users\shiva\Desktop\PROJECTS\licence-plate\plate",image_name)  #path of folder where licence plate will be saved 
		
		if cv2.waitKey(1) & 0xFF == ord('q'):					#if  the Q key is pressed the image would be saved in the folder	
			cv2.imwrite(path,roi)
			number = number+1
		
	
	cv2.imshow("video",frame)                                                       #showing frame
	k = cv2.waitKey(20) & 0xFF 							#If ESC key is pressed webcam would stop and breaks the loop
	if k== 27:
		break

cap.release()									        # Releasing webcam
cv2.destroyAllWindows()
