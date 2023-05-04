# Splice

> 我的作业需要提交 word 文档和文档转换的图片，我把报告转换成 pdf 并导出为图片，但是我没有找到简单安全的离线方式把所有图片转为一个长图，所以我使用 numpy 和 matplotlib 把所有图片拼接为长图。
>
> My homework requires submitting Word documents and document conversion images. I converted the report into PDF and exported it as images, but I couldn't find a simple and safe offline way to convert all images into a long image. Therefore, I used Numpy and Matplotlib to concatenate all images into long images.

**注意：** 这是一个简单的代码工具，该项目开源免费。

基础工具：Acaconda、Python 等。

环境配置：numpy、matplotlib 等。

## 功能说明

程序自动处理当前目录下的所有图片（需要所有图片格式和宽度相同），按照目录顺序拼接为长图。

不同图片通道数等数据不同，似乎不能对不同格式图片进行拼接。

该程序目前已经符合我个人需求，但是在未来可能会有不定期功能更新。

## 使用方法

1. 首先 clone 项目并创建虚拟环境

```
conda create -n splice python=3.8
```

2. 配置环境必要的包

```
conda install numpy matplotlib
```

3. 激活虚拟环境

```
conda activate splice
```

4. 运行代码

```
python splice.py
```

