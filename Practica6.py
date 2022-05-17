#Isaac Alejandro Gutiérrez Huerta 19110198 7E1
#Sistemas de Visión Artificial

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#Hue Saturation Value

    #ROJO
    lower_color1 = np.array([0,150,180])
    upper_color1 = np.array([15,255,255])

    #AZUL
    lower_color2 = np.array([100,90,130])
    upper_color2 = np.array([150,255,255])

    #VERDE
    lower_color3 = np.array([40,50,150])
    upper_color3 = np.array([80,255,255])
    
    mask = cv2.inRange(hsv, lower_color1, upper_color1)
    hsvRojo = cv2.bitwise_and(frame, frame, mask = mask)

    mask = cv2.inRange(hsv, lower_color2, upper_color2)
    hsvAzul = cv2.bitwise_and(frame, frame, mask = mask)
    
    mask = cv2.inRange(hsv, lower_color3, upper_color3)
    hsvVerde = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('HSV Rojo', hsvRojo)
    cv2.imshow('HSV Azul', hsvAzul)
    cv2.imshow('HSV Verde', hsvVerde)
    
    if cv2.waitKey(1) & 0xFF == ord('i'):
        break

cap.release()
cv2.destroyAllWindows()
