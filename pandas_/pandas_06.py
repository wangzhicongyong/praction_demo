
import pandas as pd
pd = pd.read_excel('standard_01.xlsx')


# print(pd['部门'])                           # 获取列名为部门 这列的值 返回值是 一个 series类型
print(pd[['部门']])                         # 返回的是一个 Dataframe 数据类型
print(pd[['部门']][0:2])                    # Dataframe数据类型也可以做切片处理
# print(pd['部门'][0:2])                      # series数据类型
print(pd[0:2])                              # 获取前两行的数据记录
row_count = print(len(pd))                 # 有多少行
col_count = print(pd.shape[1])             # 有多少列

print(pd.index)                             # 获得行索引信息
print(pd.columns)                           # 获得列索引信息   返回值是列表
# Index(['字段长度', '所属主题', '部门', '状态', '版本号', '发布时间'], dtype='object')
print(pd.columns[0])
# 字段长度

s = (pd['部门'] == '研究生院')   # 判断作用  返回 True 和 false
print(s)

# 按部门==研究生院过滤出来 数据类型是 dataframe
f = pd.loc[pd['部门'] == '研究生院']
print(f)
p = pd.loc[pd['部门'] == '研究生院']['字段长度'].get_values()   # 可以取研究生院的 dataframe 中字段的长度的值列表
print(p)
# [40 10 50 50 10 50 50 50 50 10 10 90 90 20 40 10 50 50 10 50 50 50 90 90 20]

print(pd[36:37])  # 取行