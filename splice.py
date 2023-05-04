# -*- coding: UTF-8 -*-
import os
import numpy as np
import matplotlib.image as mpimg

def load_img():
    dict = os.getcwd()
    files_list = os.listdir(dict)
    img_list = []
    for i in files_list:
        if i[-3:] in ['png','jpg','jpeg','PNG','JPG','JPEG']:
            img_list.append(i)
    return img_list

def main():
    img_list = load_img()
    n = len(img_list)
    img = [img_list[0]]*n
    for i in range(n):
        img[i] = mpimg.imread(img_list[i])
    img = tuple(img)
    img = np.vstack(img)

    mpimg.imsave('out.png', img)

if __name__ == "__main__":
    # conda activate cv
    main()

