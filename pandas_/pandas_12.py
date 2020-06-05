"""
pandas 如何遍历 dataframe
:pandas的dataframe有一个很好用的函数applymap,它可以把某个函数应用到dataframe的每一个元素上
"""
import pandas as pd

dict01 = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10]]
data = pd.DataFrame(dict01)
print(data)
# for row in data.index:
#     print(row)  # 获取行索引
#     #
#     # # data.T 将行与列对调
#     # # for date, row in data.T.iteritems():
#     # #     # print(date)    # date是行索引
#     # #     print(row)       # row是转置了的行  所以是取出的行
#     # #     # print(row[0])  # 取第一列的值
#     #
#     # # print(len(data.columns))  # 获取列数
#     # # for date, row in data.iterrows():
#     # #     for i in data.columns:   # 内循环是列名
#     # #         print('********************')
#     # #         print(i)
#     # #         # print(date)    # 获取的是行索引
#     # #         # print(row)     # 这个获取的是每一行
#     # #         print(row[i])    # 取出单元格的每一个值
#     #
#     # for date, row in data.iteritems():
#     #     # 实际date是获取的列索引
#     #     print(date)      # date是列索引
#     #     print(row)       # 获取的是每列的值
#     #     # print(row[0])  # 取第一列的值