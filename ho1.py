import cv2
import numpy as np
from matplotlib import pyplot as plt

img_1 = cv2.imread('4.png',0)
'''
ret, img = cv2.threshold(img_1,127,255,cv2.THRESH_BINARY)
edges = cv2.Canny(img,200,300)
'''
img = cv2.Canny(img_1,200,300)
ret, edges = cv2.threshold(img,127,255,cv2.THRESH_BINARY)




plt.subplot(131),plt.imshow(edges,cmap = 'gray')
plt.title('Edges Image'), plt.xticks([]), plt.yticks([])


img_2 = cv2.medianBlur(edges,5)
cimg = cv2.cvtColor(img_2,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(255,255,255),2)
    cv2.circle(img_1,(i[0],i[1]),i[2],(255,255,255),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(255,255,255),3)
    cv2.circle(img_1,(i[0],i[1]),2,(255,255,255),3)

'''
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

plt.subplot(132),plt.imshow(cimg,cmap = 'gray')
plt.title('Circ Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_1,cmap = 'gray')
plt.title('Segmentation'), plt.xticks([]), plt.yticks([])

plt.show()

