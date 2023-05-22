# Splice

> 我的作业需要提交 word 文档和文档转换的图片，我把报告转换成 pdf 并导出为图片，但是我没有找到简单安全的离线方式把所有图片转为一个长图，所以我使用 numpy 和 matplotlib 把所有图片拼接为长图。
>
> My homework requires submitting Word documents and document conversion images. I converted the report into PDF and exported it as images, but I couldn't find a simple and safe offline way to convert all images into a long image. Therefore, I used Numpy and Matplotlib to concatenate all images into long images.

**注意：** 这是一个简单的拼图代码，该项目开源免费。

编程语言：Python。

环境配置：numpy、matplotlib 等。

## 功能说明

图片拼接：读取指定文件夹中所有图片名字到catalog.txt文件并手动排序，合成横向或者纵向长图。

catalog.txt 文件记录所有图片文件名，默认生成在代码所在目录。

## 使用方法

1. 首先安装 Python

https://www.python.org/

2. 配置环境必要的模块

```
pip install numpy matplotlib
```

3. 运行代码

```
python splice.py
```

## 预期功能

- [x] 1. 指定多张图片及其顺序

- [x] 2. 简单命令行界面引导

- [ ] 3. 不同宽度图片拼接可选居中对齐或者左右对齐

- [ ] 4. 不同尺寸图片可选择拉伸或者放缩

- [ ] 5. 图片修改尺寸

- [ ] 6. word，pdf 等文档可自动处理，而不是手动转换导出图片