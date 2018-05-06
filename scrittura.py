import cv2
import time
from fpdf import FPDF
pageH = 4000
pageW = 2000
nFrames = 1500
success = True
pdf = FPDF('P', 'mm', (pageW, pageH))
pdf.add_page()
x = 0
y = 0
w = 80
h = 45
w1 = 20
h1 = 45 / 4
for g in range(nFrames):
	pdf.image('frame' + str(g) + '.jpg', x, y, w1, h1, 'JPG', '')
	x += w1
	if(x == pageW):
		x = 0
		y += h1
pdf.output('es.pdf', 'F')