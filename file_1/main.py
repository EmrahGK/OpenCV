import cv2 as cv
import numpy as np


picture = cv.imread("pic.png",0)
cv.imshow("resim (siyah beyaz)",picture)
cv.imwrite("logo_siyah_beyaz.png",picture)

"""
imread = resmi okumayı sağlar.
imshow = resmi yazdırmayı sağlar. yaklaşık= print()
imwrite = resmi kaydetmeyi sağlar. bu kadardı izlediğiniz için teşekkürler like atın abone olun iyi forumlar merhaba ben volkan konak
"""


cv.waitKey(0)
cv.destroyAllWindows()




