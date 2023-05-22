# /bin/bash
# -*- coding: UTF-8 -*-
# @AUTHOR: JINHAO
# @PROJECT: splice
# @VERSION：v0.2.0
# @CREATION DATE: 2023-04-12
# @MODIFICATION DATE: 2023-05-18
# @DETAILS: splice some images

import os
import argparse
import numpy as np
import matplotlib.image as mpimg
    
# 指定图片集路径，把所有图片文件名打印输出到 catalog.txt 文件
def load_catalog():
    global images_path
    catalog = os.listdir(images_path)
    with open('catalog.txt', 'w+', encoding='utf8')as f:
        for i in catalog:
            if os.path.splitext(i)[-1] in ['.png','.jpg','.jpeg','.PNG','.JPG','.JPEG']:
                f.write(i+"\n")
    print("序列文件生成完毕，文件路径：./catalog.txt")

# 读取图片完整相对路径加载为数组返回
def load_images_path():
    global images_path, catalog_path
    img_list = []
    with open(catalog_path, encoding='utf8') as f:
        for line in f.readlines():
            img_list.append(images_path+line.strip('\n'))
    return img_list

def get_images_complete_path():
    print(load_images_path())
    
# 垂直方向图片拼接
def v_splice_images():
    img_list = load_images_path()
    images_number = len(img_list)
    img = [img_list[0]]*images_number # 第零个图片乘图片个数作为底
    max_width = 0
    max_height = 0 
    for i in range(images_number):
        img[i] = mpimg.imread(img_list[i])
    img = tuple(img)
    img = np.vstack(img)
    mpimg.imsave('v_output.png', img)

# 水平方向图片拼接
def h_splice_images():
    img_list = load_images_path()
    n = len(img_list)
    img = [img_list[0]]*n
    for i in range(n):
        img[i] = mpimg.imread(img_list[i])
    img = tuple(img)
    img = np.hstack(img)
    mpimg.imsave('h_output.png', img)

def get_images_path():
    global images_path
    print("images_path is", images_path)

def change_images_path():
    global images_path
    original_path = images_path
    print("当前文件夹路径",images_path)
    images_path = input("请输入新的图片文件夹路径：(按0返回)")
    os.system('cls')
    if images_path == '0':
        images_path = original_path
        main()
    elif os.path.exists(images_path):
        os.system('cls')
        main()
    else:
        images_path = original_path
        os.system('cls')
        print("该目录不存在，请重新填写。")
        change_images_path()
 
def get_catalog_path():
    global catalog_path
    print("catalog_path is", catalog_path)
           
def change_catalog_path():
    global catalog_path
    if not os.path.isfile(catalog_path):
        print("当前目录下没有catalog.txt文件，请先生成该文件。")
    original_path = catalog_path
    print("当前catalog路径",catalog_path)
    catalog_path = input("请输入新的catalog路径：(按0返回)")
    
    if catalog_path == '0':
        catalog_path = original_path
        main()
    elif os.path.exists(catalog_path):
        if catalog_path[-1] == "/":
            catalog_path += "catalog.txt"
            if os.path.isfile(catalog_path):
                os.system('cls')
                main()
            else:
                os.system('cls')
                print("该目录下没有catalog.txt文件。")
                catalog_path = original_path
                print("当前catalog路径",catalog_path)
                main()
        else:
            catalog_path += "/catalog.txt"
            if os.path.isfile(catalog_path):
                os.system('cls')
                main()
            else:
                os.system('cls')
                print("该目录下没有catalog.txt文件。")
                catalog_path = original_path
                print("当前catalog路径",catalog_path)
                main()
        main()
    else:
        catalog_path = original_path
        os.system('cls')
        print("该目录不存在，请重新填写。")
        change_catalog_path()
 
def main():
    global images_path, catalog_path
    print("----------------------------------------------")
    print("图片拼接：读取指定图片文件夹路径中所有图片名字到catalog.txt文件后手动排序，合成横向或者纵向长图。")
    print("1.指定图片文件夹路径。(当前文件夹路径:", images_path, ")")
    print("2.指定catalog.txt路径。(当前catalog.txt路径:", catalog_path, ")")
    print("3.生成序列文件", catalog_path)
    print("4.按照catalog.txt纵向合并长图。")
    print("5.按照catalog.txt横向合并长图。")
    print("0.退出。")
    opt = input("请输入操作号码：")
    os.system("cls")
    if opt not in ['1','2','3','4','5','0']:
        print("输入错误，请重新输入。")
        main()
    elif opt == '1':
        change_images_path()
    elif opt == '2':
        change_catalog_path()
    elif opt == '3':
        load_catalog()
        main()
    elif opt == '4':
        v_splice_images()
        main()
    elif opt == '5':
        h_splice_images()
        main()
    elif opt == '0':
        os.system("cls")
        exit()
    else:
        print("输入错误，请重新输入！")
    
if __name__ == "__main__":
    # conda activate cv
    parser = argparse.ArgumentParser(
        description="single image process"
        )
    parser.add_argument('-i', '--images', default="./test_img/", type=str)
    parser.add_argument('-c', '--catalog', default="./catalog.txt", type=str)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')
    args = parser.parse_args()
    images_path = args.images
    catalog_path = args.catalog
    os.system('cls')
    main()
    