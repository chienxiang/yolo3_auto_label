#-*- coding: utf-8 -*-

import numpy as np
import cv2

im = cv2.imread('test3.png')
#cvtColor(const Mat& src, Mat& dst, int code)
#src來源圖,dst目標圖，尺寸大小、深度會和來源圖相同,code指定在何種色彩空間轉換
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,frame = cv2.threshold(imgray,127,255,0)
#threshold(InputArray src, OutputArray dst, double thresh, double maxval, int type)
#src輸入圖,dst輸出圖，尺寸大小、深度會和輸入圖相同,thresh閾值,maxval二值化結果的最大值type：二值化操作型態，
#共有THRESH_BINARY、THRESH_BINARY_INV、THRESH_TRUNC、THRESH_TOZERO、THRESH_TOZERO_INV五種。
contours, hierarchy = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    
#findContours( image, contours, hierarchy, mode, method, Pointoffset=Point())
#image：輸入圖，使用八位元單通道圖，所有非零的像素都會列入考慮，通常為二極化後的圖。
#contours：包含所有輪廓的容器(vector)，每個輪廓都是儲存點的容器(vector)，所以contours的資料結構為vector< vector>。
#hierarchy:可有可無的輸出向量，以階層的方式記錄所有輪廓
#mode：取得輪廓的模式，有以下幾種可選擇：
# CV_RETR_EXTERNAL：只取最外層的輪廓。
# CV_RETR_LIST：取得所有輪廓，不建立階層(hierarchy)。
# CV_RETR_CCOMP：取得所有輪廓，儲存成兩層的階層，首階層為物件外圍，
# 第二階層為內部空心部分的輪廓，如果更內部有其餘物件，包含於首階層。
# CV_RETR_TREE：取得所有輪廓，以全階層的方式儲存。
#method:儲存輪廓點的方法
# CV_CHAIN_APPROX_NONE：儲存所有輪廓點。
# CV_CHAIN_APPROX_SIMPLE：對水平、垂直、對角線留下頭尾點，所以假如輪廓為一矩形，只儲存對角的四個頂點。
print ("there are "+ str(len(contours)) + " contours")

cnt = contours[0]
print ("there are " + str(len(cnt)) + " points in contours[0]")
print (cnt)
 
cnt = contours[1]
print ("there are " + str(len(cnt)) + " points in contours[1]")
print (cnt)
 
cv2.imshow('im', im)
cv2.waitKey(0)
cv2.destroyAllWindows()