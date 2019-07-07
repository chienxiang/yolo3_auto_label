#-*- coding: utf-8 -*-
import numpy as np
import cv2

# 讀取圖檔
img = cv2.imread('dog.jpeg')

# 讓視窗可以自由縮放大小
cv2.namedWindow('camera', cv2.WINDOW_NORMAL)
cv2.imshow('camera',img)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()