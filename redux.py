# Cinema Redux 			
# Created by Davide Bonafede	
import cv2
import time
import numpy as np
#Video file importing
vidcap = cv2.VideoCapture('Happy Family.mkv')
count = 0
success = True
firstLine = 1
# width and heigth of resized frames
w = 80
h = 45
z = 0
nFrameforLine = 60
oneFrameEvery = 24
success,image = vidcap.read()
while success:
	if(count % oneFrameEvery == 0):
		image = cv2.resize(image, (w, h))	# image resize
		if z == 0:							# first image of the line 
			imageLine = image
			z += 1
		else:
			imageLine = np.concatenate((imageLine, image), axis=1)
			z += 1
			if z == nFrameforLine:			# the line is finished
				if firstLine:
					Image = imageLine
					firstLine = 0
					z = 0
				else:
					Image = np.concatenate((Image, imageLine), axis=0)
					z = 0
	success,image = vidcap.read()
	count += 1
# fill with black missing frames to complete image
for x in range(nFrameforLine - z):
	imageLine = np.concatenate((imageLine, np.zeros((h,w,3), np.uint8)), axis=1)
Image = np.concatenate((Image, imageLine), axis=0)
cv2.imwrite("redux.jpg", Image)
