import cv2

gambar = cv2.imread('blackping.jpeg')

# x = int(input("masukan kordinat "))

cv2.imshow('tampil',gambar)
cv2.waitKey(0)
cv2.destroyWindow()