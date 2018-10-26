import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

img_1 = cv2.imread(sys.argv[1],0)
plt.subplot(331),plt.imshow(img_1,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

ret, img = cv2.threshold(img_1,127,255,cv2.THRESH_BINARY)
plt.subplot(332),plt.imshow(img,cmap = 'gray')
plt.title('Threshold Image'), plt.xticks([]), plt.yticks([])

edges = cv2.Canny(img,200,300)
plt.subplot(333),plt.imshow(edges,cmap = 'gray')
plt.title('Canny Image'), plt.xticks([]), plt.yticks([])

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img_1,(i[0],i[1]),i[2],(255,255,255),2)
    # draw the center of the circle
    cv2.circle(img_1,(i[0],i[1]),2,(255,255,255),3)
    break

plt.subplot(334),plt.imshow(img_1,cmap = 'gray')
plt.title('Hough Tranform '), plt.xticks([]), plt.yticks([])
'''
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''


img_1_1 = cv2.imread(sys.argv[1],0)
'''
ret, img = cv2.threshold(img_1,127,255,cv2.THRESH_BINARY)
edges = cv2.Canny(img,200,300)
'''
img = cv2.Canny(img_1_1,200,300)
plt.subplot(335),plt.imshow(img,cmap = 'gray')
plt.title('Canny Image _ 2'), plt.xticks([]), plt.yticks([])

ret, edges = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.subplot(336),plt.imshow(edges,cmap = 'gray')
plt.title('Threshold Image _ 2'), plt.xticks([]), plt.yticks([])


circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img_1,(i[0],i[1]),i[2],(255,255,255),2)
    # draw the center of the circle
    cv2.circle(img_1,(i[0],i[1]),2,(255,255,255),3)
    break


plt.subplot(337),plt.imshow(img_1,cmap = 'gray')
plt.title('Hough Image Final'), plt.xticks([]), plt.yticks([])

plt.show()

