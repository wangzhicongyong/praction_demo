import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
            'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
# 字典的键就是列名
df = pd.DataFrame(ipl_data)
print(df)
# 按照年份Year字段分组
print(df.groupby('Year'))
# 查看分组结果--返回值是一个字典
print(df.groupby('Year').groups)
# 根据建可以求出2014年所对应的数据
print(df.groupby('Year').groups[2014].get_values())
# [0 2 4 9]
# 取出 0 2 4 9 行的记录
s = df.loc[df.groupby('Year').groups[2014].get_values(), :]
print(s)

# 这里也是取出2014年的数据记录, loc是两个参数
p = df.loc[df['Year'] == 2014, :]
print(p)