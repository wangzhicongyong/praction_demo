import pandas as pd
import numpy as np

#  创建一个空的系列
s = pd.Series()
print(s)

# # 从ndarray创建一个系列
data = np.array(['a', 'b', 'c', 'd'])
print(data)  # ['a' 'b' 'c' 'd'] ndarry数组类型
print(data[0])  # a  依然是可以以列表的索引取值

s = pd.Series(data)  # 将ndarry 数组转换为 series数据类型
print(s)

# 可以自己设置自定义的 行索引的值
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)

# 从字典创建一个系列  index 就是keys
data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)

# 从标量创建一个系列
s = pd.Series(5, index=[0, 1, 2, 3, 4])
print(s)

# 使用索引检索元素
s = pd.Series([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
print(s)
print('********************************************************')

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s.index = ['k', 'm', 'h', 'y', 't']  # 可以替换索引值
print(s)
print(s[0])  # 直接取值
print(s[:3])  # 取前3行的值
print(s[-3:])  # 取后3行的值

# 使用标签检索数据
# print(s['a'])  # 取叫a行的值
# print(s[['a', 'c', 'd']])