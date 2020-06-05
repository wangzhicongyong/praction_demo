

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df1 = DataFrame({'key': ['X', 'Y', 'Z'], 'data_set_1': [1, 2, 3]})
# print(df1)

df2 = DataFrame({'key': ['X', 'B', 'C'], 'data_set_2': [4, 5, 6], 'c': [2, 5, 4]})
# print(df2)


# 感觉这个就像 操作 sql 的感觉一样
# 找到一个外键 然后将两条数据拿到手
print(pd.merge(df1, df2))  # 只能有一个外键 有多个 则相同的字段的值 必须相同否则为空
print('********************************')
'''
   data_set_1 key  data_set_2
0           1   X           4
'''

# 第二个参数 on 代表 要在 哪一个 列上 进行 merge
# print(pd.merge(df1, df2, on='data_set_1')) # 报错

# inner 拿出的是两边都有的值
print(pd.merge(df1, df2, on='key', how='inner'))
'''
   data_set_1 key  data_set_2
0           1   X           4
'''

# left 按照left的dataframe为基准，右边值为空的话就默认nan
print(pd.merge(df1, df2, on='key', how='left'))
'''
   data_set_1 key  data_set_2
0           1   X         4.0
1           2   Y         NaN
2           3   Z         NaN
'''
# 同理 right 按照右边为基准
print(pd.merge(df1, df2, on='key', how='right'))
'''
   data_set_1 key  data_set_2
0         1.0   X           4
1         NaN   B           5
2         NaN   C           6
'''

# outer 将 left right 的结合， 所有的key都拿出来，哪边缺失，就补充nan
print(pd.merge(df1, df2, on='key', how='outer'))
