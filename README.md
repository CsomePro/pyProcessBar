# pyProcessBar
## 简述
pyProcessBar是使用Python制作的，可用于IDE内，进度条显示库
## 效果展示
```python
Processing[##################------------]	6047/10000	60.47%	0:00:01	 7521.22/s
```
## 快速入门
方法一：
```python
import pyProcessBar
bar = pyProcessBar.ProcessBar()
for k in range(n):
    # do something
    bar.bar_print(k+1, n)
```
方法二：
```python
import pyProcessBar
bar = pyProcessBar.ProcessBar()
for k in range(n):
    # do something
    bar.next()
```
## 使用文档
这个库中定义了ProcessBar类，初始化有3个值
``` python
bar = pyProcessBar.ProcessBar(process_tip='Processing', process_char='#', n=0)
```
`process_tip`进度条提示（标题），`process_char`进度条填充字符，`n`总迭代次数
