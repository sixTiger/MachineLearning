#mac  Anaconda matplotlib 中文乱码问题
### 这里所有的操作都是以黑体字体为例
### 一. 准备一个中文字体
### 二. 清除字体缓存
>###MAC默认的缓存目录

```shell
~/.matplotlib/
```
### 三. 添加字体到 `matplotlib` 中
>###1. 添加字体文件 matplotlib的默认安装目录在 
>```c
/anaconda2/lib/python2.7/site-packages/matplotlib/mpl-data
>```
>###把字体放在相应的目录`fonts/ttf`中即可
>###2. 编辑配置文件 `matplotlibrc `
>###找到 `font.sans-serif`,默认情况下配置如下：
>```c
#font.sans-serif     :DejaVu Sans, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
```
>###修改为：
>```c
font.sans-serif     : SimHei, DejaVu Sans, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif

>```
>其中 `SimHei,`为我们准备的中文字体

###四重启 Anaconda

>###然后在代码中添加下边语句
>```c
#!/usr/bin/python
# -*- coding: UTF-8 -*-
>```
>###重新运行代码即可在图标中显示中文

