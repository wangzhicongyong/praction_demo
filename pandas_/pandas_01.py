

import pandas as pd
import numpy as np
# pd = pd.read_excel('standard_template.xlsx')
# print(pd)
# hearder = None 这个参数如果是加了 代表该文件没有标题字段，直接读取的是文件里面的数据
# pd = pd.read_excel('standard_01.xlsx')
# print(pd)  # 读取文件里面的数据
# notnull()，返回值是布尔型的矩阵，再取df[布尔型矩阵]返回的是id为非空的行
# print df[df['id'].notnull()

# print(pd.notnull())   # 这个生成的是一个bool值的二维矩阵

# where是pandas的过滤函数  参数是过滤的条件 不满足的默认为 NaN
# df = pd.where(pd.notnull(), None)   # 把所有为空的列的值改为None

# df = pd.where(pd.notnull(), None)
# print(df)

# isnull 是判断文件或者数组有没有缺失值 如果有 则为True
# print(df.isnull())   # 返回值是 布尔值的数组

# 删除一列： one
# del(df['one'])
# print(df)

# 调用pop方法删除一列
# df.pop('two')
# print(df)

data = {'name': ['Joe', 'Mike', 'Jack', 'Rose', 'David', 'Marry', 'Wansi', 'Sidy', 'Jason', 'Even'],
        'age': [None, None, 18, None, 15, None, 41, None, 37, None],
        'gender': [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        'isMarried': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)
print(df)
# df1 = df[pd.notnull(df['age'])]
# print(df1)
df.dropna(subset=['age'], inplace=True)
print(df)