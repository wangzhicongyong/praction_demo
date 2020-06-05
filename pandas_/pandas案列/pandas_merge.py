
"""
pandas的merge()函数的详解
"""

import pandas as pd

df1 = pd.DataFrame({'A': ['a', 'a', 'a', 'a', 'a'], 'B': [0, 1, 2, 3, 4], 'C': [1, 1, 1, 2, 3]})
print(df1)

# 新签
df2 = pd.DataFrame({'A': ['a', 'a', 'b', 'c', 'd'], 'B1': [0, 1, 2, 3, 4], 'C': [1, 1, 1, 2, 2]})
print(df2)

# on的参数是设置连接键的，可以是多个键做标准, 都是会进行多次匹配
df = pd.merge(df1, df2, on=['A', 'C'], how='inner')
print(df)


# 方法一
# df = pd.merge(df1, df2, on=['key', '订单'], how='right')
# print(df)

# 方法二 和方法一是等价的，以右边为标准，尽可能在左边匹配
df = df1.merge(df2, on=['A', 'C'], how='right')
print(df)