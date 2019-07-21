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
hull = cv2.convexHull(cnt)  #找凸多邊形
#convexHull(InputArray points, OutputArray hull, bool clockwise=false, bool returnPoints=true)
#points：輸入資訊，可以為包含點的容器(vector)或是Mat。
#hull：輸出資訊，包含點的容器(vector)。
#lockwise：方向旗標，如果true是順時針，false是逆時針
print ("after convexHull, there are " + str(len(hull)) + " points")
cv2.drawContours(im,[hull],0,(255,0,0),-1)
 
cv2.imshow('im', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
