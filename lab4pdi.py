#! /usr/bin/python
#TODA  LAS FOTOS DEBEN TENER EL MISMO TEXTO ESCRITO SOLO SE CAMBIARA LA SUPERFICI
#DEL TEXTO
from SimpleCV  import Image, Camera, Display, time, cv2
import numpy as np
import matplotlib.pyplot as plt

prueba=Image("harriscuadrado1.jpg")
prueba1=Image("harriscuadrado2.jpg")
prueba2=Image("harriscuadrado3.jpg")
prueba3=Image("harriscuadrado4.jpg")
prueba4=Image("harriscuadrado5.jpg")
prueba5=Image("harriscuadrado6.jpg")
prueba6=Image("harriscuadrado7.jpg")
prueba7=Image("harriscuadrado8.jpg")
prueba8=Image("harriscuadrado9.jpg")

escalagris=prueba.grayscale()
escalagris.save("gray.jpg")

img = cv2.imread('harriscuadrado1.jpg',0)
imagen=prueba[100,100]
print imagen

rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

#cv2.imshow('img',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
rows,cols = img.shape

img = cv2.imread('harriscuadrado1.jpg')


pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
#aproximacion  a fin , metodo para la estabilizavion de la imagen y/o la alinacion
