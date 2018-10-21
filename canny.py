import cv2
import numpy as np
from matplotlib import pyplot as plt

img_1 = cv2.imread('4.png',0)
ret, img = cv2.threshold(img_1,127,255,cv2.THRESH_BINARY)
edges = cv2.Canny(img,200,300)


img_2 = cv2.medianBlur(edges,5)
cimg = cv2.cvtColor(img_2,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img_1,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img_1,(i[0],i[1]),2,(0,0,255),3)
'''
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
plt.subplot(121),plt.imshow(edges,cmap = 'gray')
plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_1,cmap = 'gray')
plt.title('Hough Image'), plt.xticks([]), plt.yticks([])

plt.show()

