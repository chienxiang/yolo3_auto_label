#-*- coding: utf-8 -*-
import numpy as np
import cv2
  
im = cv2.imread('test3.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print ("there are " + str(len(contours)) + " contours")
 
cnt = contours[0]
print ("there are " + str(len(cnt)) + " points in contours[0]")
approx = cv2.approxPolyDP(cnt,10,True) #原輸出精度30圖為正五邊形
#approxPolyDP(InputArray curve, OutputArray approxCurve, double epsilon, bool closed)
#InputArray curve:一般是由图像的轮廓点组成的点集
#OutputArray approxCurve：表示输出的多边形点集
#epsilon：主要表示输出的精度，就是另个轮廓点之间最大距离数，5,6,7，，8，，,,，
#closed：表示输出的多边形是否封闭

print ("after approx, there are " + str(len(approx)) + " points")
print (approx)
cv2.drawContours(im,[approx],0,(255,0,0),-1)
#drawContours( image,  contours , int contourIdx,  color, int thickness, int lineType, hierarchy, int maxLevel)
#mage：輸入輸出圖，會將輪廓畫在此影像上。
#contours：包含所有輪廓的容器(vector)，也就是findContours()所找到的contours。
#contourIdx：指定畫某個輪廓。
#color：繪製的顏色。
#lineType：繪製的線條型態。
#hierarchy：輪廓階層，也就是findContours()所找到的hierarchy。
#maxLevel：最大階層的輪廓，可以指定想要畫的輪廓，有輸入hierarchy時才會考慮，輸入的值代表繪製的層數。

 
cnt = contours[1]
print ("there are " + str(len(cnt)) + " points in contours[1]")
approx = cv2.approxPolyDP(cnt,30,True)
print ("after approx, there are " + str(len(approx)) + " points")
print (approx)
cv2.drawContours(im,[approx],0,(0,255,0),-1)
 
cv2.imshow('im', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
