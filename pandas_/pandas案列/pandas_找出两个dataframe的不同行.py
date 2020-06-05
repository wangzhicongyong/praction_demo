
"""
第一种情况，当两个dataframe之间存在交集，且是包含与被包含之间的关系时；
第二种情是两者不是包含关系，但是确实存在交集。
当然第一种情况的使用方法也适用于第二种。
在这两种情况下，如何从df1中删除df1与df2之间相同的元素，仅保留df1中独有的元素？？
"""

import pandas as pd
dt1 = {"course": ['math', 'english', 'chinese', 'physics', 'gym', 'eee', 'math'],
       "score": [98, 90, 88, 89, 99, 100, 88]
       }

df1 = pd.DataFrame(dt1)
print(df1)

dt2 = {"course": ['math', 'english', 'chemistry', 'physics', 'history'],

       "score": [98, 90, 82, 89, 81]}

df2 = pd.DataFrame(dt2)

print(df2)

### 重要的事情说三遍： 两个dataframe之间的字段必须是一样的

# 代码中subset对应的值是列名，表示只考虑这两列，将这两列对应值相同的行进行去重。默认值为subset=None表示考虑所有列
# 如果两个dataframe是包含的关系时,则只需要用一次append
# 获取到 df1 和 df2 的交集（在df1中去除含有df2数据源的行）
df4 = df1.append(df2)
df5 = df4.append(df2)
print(df5)
# 只有当 course，score 的两列的值 都是 一样的 行 才会被过滤掉
df3 = df5.drop_duplicates(subset=['course', 'score'], keep=False)
print(df3)

    # course  score
# 2  chinese     88
# 4      gym     99
# 5      eee    100
# 6     math     88