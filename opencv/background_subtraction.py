#-*- coding: utf-8 -*-
import cv2
import numpy as np
ph1 = "/home/tony/Documents/data/img_3/1.jpg"
ph2 = "/home/tony/Documents/data/img_3/5.jpg"

threshod= 20 

img = cv2.imread(ph2,3) #RGB
s1 = cv2.imread(ph1,0)  #灰階
s2 = cv2.imread(ph2,0)

emptyimg = np.zeros(s1.shape,np.uint8) #uint8 0~255
#zeros(shape, dtype=float, order='C')
#回傳一給定形狀和型別的用0填充的陣列

#fgbg = cv2.BackgroundSubtractorMOG()

#dest??
def pic_sub(dest,s1,s2,img):
    for x in range(dest.shape[0]):
        for y in range(dest.shape[1]):
            if(s2[x,y] > s1[x,y]):
                dest[x,y] = s2[x,y] - s1[x,y]
            else:
                dest[x,y] = s1[x,y] - s2[x,y]

            if(dest[x,y] < threshod):
                img[x,y] = 255
                dest[x,y] = 0
            else:
                dest[x,y] = 255



pic_sub(emptyimg,s1,s2,img)

cv2.namedWindow("s1")
cv2.namedWindow("s2")
cv2.namedWindow("result")
cv2.namedWindow("img")

cv2.imshow("s1",s1)
cv2.imshow("s2",s2)
cv2.imshow("result",emptyimg)
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()