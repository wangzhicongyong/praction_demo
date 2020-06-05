import pandas as pd
import numpy as np
data = {'name': ['Joe', 'Mike', 'Jack', 'Rose', 'David', 'Marry', 'Wansi', 'Sidy', 'Jason', 'Even'],
        'age': [25, 32, 18, np.nan, 15, 20, 41, np.nan, 37, 32],
        'gender': [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        'isMarried': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
df.info()
print(df)

# 取列的值
# df = df['name'].get_values()
# print(df)
#
# for i in df:
#     print(i)

df = df[['name', 'age']]
df = df[['name', 'age']].get_values()
print(df)