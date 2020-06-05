
"""
先根据某个字段分组全部取出来，然后某一组合并成一条数据，其中某列的 值 全部累加
"""

import pandas as pd

# Your data
data = pd.DataFrame({'column1': ['1', '1', '2', '2'],
       'column2': [4, 5, 6, 7]})

print(data)

# df = data.groupby('column1').agg('count')
# df = data.groupby('column1').get_group('1')
# print(df)   # 返回值是一个分组对象，可以调用一些方法

# Grouped dict
data_dict = data.groupby('column1').column2.apply(list).to_dict()
print(data_dict)   # {'key1': ['value1', 'value2'], 'key2': ['value3', 'value3']}
fangyuan_list = []
shijiruzhu_list = []

for i in data_dict.keys():  # 返回值是列表
       fangyuan_list.append(i)
       shijiruzhu_list.append(sum(data_dict[i]))
data = pd.DataFrame({'column1': fangyuan_list,
       'column2': shijiruzhu_list})

print(data)