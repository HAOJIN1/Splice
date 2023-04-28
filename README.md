# Splice

> 我的作业需要交 word 报告的图片，但是我没有找到简洁并且方便的离线的安全方式来把我的报告转为长图，所以我首先把报告转换成pdf并导出为图片，然后使用 numpy 和matplotlib 把所有图片拼接为长图。（我之前尝试使用 opencv，但是很明显使用 numpy 的 vstack 更加方便）
>
> For my assignment, I needed to turn in images for a word report, but I couldn't find a clean and easy offline secure way to turn my report into a long graph, so I first converted the report into a pdf and exported it as an image, then used numpy and matplotlib to stitch all the images into a long graph. (I tried using opencv before, but it was obvious that vstack with numpy was more convenient)



**注意：** 这是一个当前在使用时有很多限制的代码工具，不过在后期我抽时间会为之增加很多功能，这是免费开源的工具。



基础工具：Acaconda、Python 等。

环境配置：numpy、opencv 等。



## 创建虚拟环境

```
conda create --name splice --file requirements.txt
```

解释：该 `requirements.txt` 列举的库是我在课程实验中的一个环境所配置的库。如下是用命令安装的必要的库：

```
conda install numpy
conda install -c conda-forge opencv
```



## 进入虚拟环境

```
conda activate splice
```



## 图片处理

新版本：程序自动处理当前目录下的所有图片，按照默认顺序拼接在一起。

根据顺序把需要合成长图的 `png` 图片命名为 ：`01.png、02.png……` （我在使用过程中所有图片大小都相等，不是这种情况可能无法达到预期效果）



## 合成长图

通过修改 `splice.py` 文件中 `page_num` 的值设置图片数量，在虚拟环境或者 `Python` 环境中使用以下命令生成长图

```python
python splice.py
```

