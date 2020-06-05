import pandas as pd

# 创建DF
d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
   'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
   'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
   'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

df = pd.DataFrame(d)
print(df)
# 测试描述性统计函数
print(df.sum())
# 传入axis=1将会按行进行求和运算
print(df.sum(1))
print(df.mean())
print(df.mean(1))

df = pd.DataFrame(d)
# 获取到的是数组的所有信息
print(df.describe())
# 针对字段类型是 object
print(df.describe(include=['object']))
print(df.describe(include=['number']))