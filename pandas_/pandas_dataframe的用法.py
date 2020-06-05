
import pandas as pd
# 创建一个空的DataFrame, 类似于表格的数据类型
df = pd.DataFrame()
print(df)

# # 从列表创建DataFrame，会生成行索引，列索引
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])   # 指定行索引，列索引默认从0开始
print(df)

data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])  # columns是列名
# 行索引没有指定用默认的，列索引指定用columns
print(df)

data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)
print(df)  # dataframe 数据类型
print(df['Name'])  # 取出name列的值
print(df['Name'] == 'Bob')  # 这个是可以判断 name列中是否有叫 Bob的，有则返回 True
print(df[df['Name'] == 'Bob'])  # 这个可以取出列中Bob的行

# 字典的值 key是列 value对应每列的值   行索引没有指定 用默认的
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

# # 从字典来创建DataFrame key是列名 value是对应的值
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'])
df.info()
print(df)

# data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#         'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(data)
# print(df)