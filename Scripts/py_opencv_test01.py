import cv2 as cv
import numpy

img= cv.imread("C:\\Users\\jweif\\Desktop\\IMG_1252.JPG",0)
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.imshow('image',img)
k = cv.waitKey(10000)

if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()