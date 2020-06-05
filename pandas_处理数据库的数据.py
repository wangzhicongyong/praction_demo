

import pandas as pd
from sqlalchemy import create_engine

# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/film')
# 查询语句，选出employee表中的所有数据
# sql = ''' select * from shaxian_info; '''
sql = ''' select * from shaxian_info where BD名称='彭友焰'; '''
# read_sql_query的两个参数: sql语句， 数据库连接
df = pd.read_sql_query(sql, engine)
# 输出shaxian_info表的查询结果 将整张表的数据都可以读出来
# 然后使用pandas来做处理 再然后存储到 数据库里面去
print(df)

# 新建pandas中的DataFrame, 只有id,num两列
df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['zhangsan', 'lisi', 'wangwu', 'zhuliu']})

# 将新建的DataFrame储存为MySQL中的数据表，储存index列 则index=True
df.to_sql('mydf', engine, index=False)
print('Read from and write to Mysql table successfully!')