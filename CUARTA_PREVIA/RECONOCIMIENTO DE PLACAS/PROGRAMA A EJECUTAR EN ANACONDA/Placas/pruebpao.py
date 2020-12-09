# RECONOCIMIENTO DE PLACAS

# Instalación de OpenCV
# pip install opencv-contrib-python

# Instalación de la librería de Tesseract
# pip install pytesseract

# Instalación del programa Tesseract
# Instalar el programa Tesseract.exe

# Importar librería OpenCV
import cv2

# Importar Librería para reconocimiento de caracteres
import pytesseract

#Necesaria para ejecutar pytesseract desde windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\paola\Downloads\TRABAJO FINAL COMPUATCION BLANDA_2020\Trabajo_2(reconocimiento de placas)\Placas\tesseract'
#Array para la placa detectada
placa = []
#Lee la imagen y la convierte en una matriz 
image = cv2.imread('fr.jpg')
#Cambia la imagen de bgr a una escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Eliminacion de ruido en la imagen
gray = cv2.blur(gray,(3,3))
#Deteccion de bordes con valores umbral /Invierte el color de la imagen
canny = cv2.Canny(gray,150,200)
#Engrosa las areas blancas para detectar mejor los contornos
canny = cv2.dilate(canny,None,iterations=1)
#Guarda los contornos en la siguiente variable 
cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#Dibuja todos los contornos encontrados
#cv2.drawContours(image,cnts,-1,(0,255,0),2)

#Recorre los contornos dibujados y elimina los innecesarios
for c in cnts:
#Con la siguiente funcion de area define el area a buscar
  area = cv2.contourArea(c)
#Define el rectangulo con cuatro vertices
  x,y,w,h = cv2.boundingRect(c)
#Determina los vertices del contorno
  epsilon = 0.09*cv2.arcLength(c,True)
#Cuenta o enumera los vertices del area 
  approx = cv2.approxPolyDP(c,epsilon,True)
#Por tanteo se define el contorno con el tamaño deseado es decir restrigimos el for  
#Ademas se asegura de que el contorno tenga cuatro vertices
  if len(approx)==4 and area>9000:
#Se imprime el area de la figura
    print('area=',area)
#Relacion de 2,4 en placas respecto al ancho y la altura
    aspect_ratio = float(w)/h
    if aspect_ratio>2.4:
#Almacena el contorno encontrado en escala de grises 
      placa = gray[y:y+h,x:x+w]
#Convierte el rectangulo encontrado a texto con tysseract     
      text = pytesseract.image_to_string(placa,config='--psm 11')
      print('PLACA: ',text)
#Para visualizar la placa en pantalla
      cv2.imshow('PLACA',placa)
#Para mover la imagen a la posicion (780,10) en la pantalla
      cv2.moveWindow('PLACA',780,10)
#Para seleccionar en la imagen el contorno rectangular
      cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
#Para colocar el texto extraido de la imagen,en la imagen del coche
      cv2.putText(image,text,(x-20,y-10),1,2.2,(0,255,0),3)

#Para imprimir la imagen o fotografia del coche
cv2.imshow('Image',image)
#Para mover la fotografia
cv2.moveWindow('Image',45,10)
#Para cerrar el proceso con alguna tecla presionada
cv2.waitKey(0)
