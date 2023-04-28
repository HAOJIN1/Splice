# -*- coding: UTF-8 -*-
import cv2
import os
import numpy as np

def load_img():
    dict = os.getcwd()
    files_list = os.listdir(dict)
    img_list = []
    for i in files_list:
        if i[-3:] in ['png','jpg']:
            img_list.append(i)
    return img_list
    
def main():
    load_img()
    n = len(load_img())
    # n = page_num
    # if n < 10:
    #     imgList = [r'0_Page_'+str(i+1)+".png" for i in range(n)]
    # if n >= 10 and n < 100:
    #     imgList = [r'0_Page_'+str(i+1).zfill(2)+".png" for i in range(n)]
    imgList = load_img()
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
    # conda activate cv
    main()

