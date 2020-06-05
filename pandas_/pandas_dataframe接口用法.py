
import pandas as pd

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

# 先指定数据类型
# dtype_dic= {'subject_id': str,
#             'subject_number' : 'float'}
# df = pd.read_csv(yourdata, dtype = dtype_dic)

# 当列存在nan时则会默认把该列转化为float数据类型
df = pd.DataFrame(d)
print(df)
print(df.notnull())   # 判断是否有nan的值  则返回 false
print(df.where(df.notnull(), 0))   # 把所有为空的列的值改为None
print(df['one'])
print(df[['one', 'two']])  # 如果是取的多列参数是列表形式

# 取行的记录是   用 ：
# 标签索引切片：前闭后闭
print(df[2:4])  # 取2,3行的记录
print(df[:'a'])  # 根据标签索引切片
print(df['a':'b'])  # 根据标签索引切片 取行记录

# 如果是指定了行索引的话 比如定义了  index=
print(df.loc['a'])
print(df.loc[['a', 'b']])
#    one  two
# a  1.0    1
# b  2.0    2