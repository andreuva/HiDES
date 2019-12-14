import numpy as np 
import cv2
import glob

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('animacion_reflexion_total.avi' ,fourcc ,15 ,(1200,1200))

lista = sorted(glob.glob('*'))

for imag in lista:
	img = cv2.imread(imag)
	# print(imag)
	# img = cv2.resize(img,(1000,1000)) #redimensionar
	out.write(img)

out.release()
