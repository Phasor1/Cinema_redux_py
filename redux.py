import cv2
import time
from fpdf import FPDF
vidcap = cv2.VideoCapture('Il Viale Del Tramonto.mp4')
count = 0
success = True
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
x = 0
y = 0
w = 80
h = 45
z = 0
nFrames = 1500
sFactor = 16
while success:
	if(count % 24 == 0):
		image = cv2.resize(image, (w, h))
		cv2.imwrite("frame%d.jpg" % z, image)
		z += 1
	success,image = vidcap.read()
	print ('Read a new frame: ', success)
	if(z == nFrames): 
		break
	count += 1
z = 0
for g in range(nFrames):
	if(g % 42 == 0 and g != 0): 
		x = 0 
		y += h
	pdf.image('frame' + str(g) + '.jpg', x / sFactor, y / sFactor, w / sFactor, h / sFactor, 'JPG', '')
	z += 1
	x +=  w
pdf.output('es.pdf', 'F')
