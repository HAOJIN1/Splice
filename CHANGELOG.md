# CHANGELOG

新增（ Features ）：新增功能。

修复（ Fixed ）：修复 bug。

变更（ Changed ）：对于某些已存在功能所发生的逻辑变化。

优化（ Refactored ）：性能或结构上的优化，并未带来功能的逻辑变化。

即将删除（ Deprecated ）：不建议使用 / 在以后的版本中即将删除的功能。

删除（ Removed ）：已删除的功能。


## 1.0.0 - 2023-05-22

> 简介：设计了一个简单的命令行界面，通过步骤引导完成相同格式和大小的图片集合成长图。

### Features

- 设计了 catalog.txt 文件读取图片名并手动处理图片顺序。
- 修改 main() 函数为界面。
- 添加了 argparse 模块及其部分参数的输入功能。
- 添加了 load_catalog() 函数生成 catalog 文件。
- 添加了 v_splice_images() 函数纵向合成图片。
- 添加了 h_splice_images() 函数横向合成图片。
- 添加了 load_images_path() 函数读取图片完整路径。
- 添加了三个 get 函数作为 images_path、catalog_path 和 get_images_complete_path 的查看接口。

### Refactored

- 优化了文件后缀识别方法。
- 优化了 README 内容。

### Changed

- load_img()函数变更为load_images_path()。

## 0.2.0 - 2023-05-04

> 简介：支持部分非英文路径图片合成长图，对 PDF 导出的图片可以直接合成长图。

### Features

- 增加了 PNG、JPG、JPEG、jpeg 等图片格式后缀识别。

### Refactored

- 完善了 README 的排版。

### Changed

- 用 matplotlib 替代了 opencv，支持中文路径。

## 0.1.1 - 2023-04-29

> 简介：自动识别当前目录下的 png 和 jpg 格式的图片文件，如果所有图片格式相同且等宽则按照顺序合成为一个长图，否则报错。

### Changed

- 自动识别当前目录下所有 png 和 jpg 图片文件

- 按照目录顺序自动合成长图

## 0.1.0 - 2023-03-22

> 简介：将尺寸相同的图片重命名为指定格式，并在主程序编辑图片数量，执行代码将相关图片合成为长图。

### Features

- 合成长图的基本功能。

- 支持识别 png、jpg 后缀。