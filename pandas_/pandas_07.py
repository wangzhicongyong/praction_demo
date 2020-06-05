
import pandas as pd
import numpy as np

data = {'name': ['Joe', 'Mike', 'Jack', 'Rose', 'David', 'Marry', 'Wansi', 'Sidy', 'Jason', 'Even'],
        'age': [25, 32, 18, np.nan, 15, 20, 41, np.nan, 37, 32],
        'gender': [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        'isMarried': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
# 数组的基本信息
df.info()
print(df)
print('*****************************************')
# df.index
# df.columns
# df.T   # 行与列对调
print(df.axes)   # 获取行索引和列索引

# # 选取age>30的记录
# df = df[df['age'] > 30]
# print(df)
# # 选取出所有age大于30，且isMarried为no的行  条件用括号括起来
# df = df[(df['age'] > 30) & (df['isMarried'] == 'no')]
# print(df)
#
# # 选取出所有age为20或32的行
# df = df[(df['age'] == 20) | (df['age'] == 32)]
# print(df)
#
# ## 取列的值
# df = df['name']    # 根据列名称
#
# # 转换类型
# # df = df['age'].astype('float').get_values()    # 这里因为有缺失值 会报错
# df = df['gender']
# print(df)
# df = df[['name', 'age']]  # 选取多个列的值