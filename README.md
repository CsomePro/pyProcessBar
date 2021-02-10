# pyProcessBar
## 简述
pyProcessBar是使用Python制作的，可用于IDE内，进度条显示库
## 效果展示
```python
Processing[##################------------]	6047/10000	60.47%	0:00:01	 7521.22/s
```
## 使用方法
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
