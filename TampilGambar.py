import cv2
#import numpy as np

#membuat sebuah fungsi yang bernama nothing
def nothing (x):
    pass

#membuat window dengan nama "Tracking"
cv2.namedWindow("tampil")

while True:

#membuat variable frame
    frame = cv2.imread('blackping.jpeg')

#menampilkan
    cv2.imshow("tampil", frame)

    key = cv2.waitKey(1)
    if key ==27:
        break

cv2.destroyAllWindows()