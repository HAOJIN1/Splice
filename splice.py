import cv2
import os
import numpy as np

def c(page_num):
    n = page_num
    imgList = [str(i+1).zfill(2)+".png" for i in range(n)]

    img = [imgList[0]]*n
    for i in range(n):
        img[i] = cv2.imread(imgList[i])

    img = tuple(img)
    img = np.vstack(img)

    cv2.imwrite('out.png', img)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    page_num = 10
    c(page_num)
