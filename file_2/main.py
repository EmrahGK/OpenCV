import cv2 as cv
import numpy as np

resim = cv.imread("kus.jpg")

cv.imshow("resim",resim)

print(resim[230,80])
print(f"Boyut: {resim.size}")
print(f"Özellik: {resim.shape}")
print(f"Veri tipi {resim.dtype}")


cv.waitKey(0)
cv.destroyAllWindows()