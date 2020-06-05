
# 导入必要模块
import pandas as pd
from sqlalchemy import create_engine

# 初始化数据库连接，使用pymysql模块
db_info = {
           'user': 'root',
           'password': '123456',
           'host': 'localhost',
           'port': 3306,
           'database': 'film'}

# 创建数据库连接
engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % db_info, encoding='utf-8')

# 读取本地CSV文件  engine='python'处理路径有中文问题
filename_xin = 'E:\python\新签.xlsx'
filename_tui = 'E:\python\合租退房.xlsx'
filename_xu = 'E:\python\合租续签.xlsx'
df = pd.read_excel(filename_xin)

# df.ix[df['代理商补贴率'] == '-', '代理商补贴率'] = '0.00%'  # 刷选
# df = df.where(df.notnull(), 0)  # 将dataframe为空的全部用0代替
print(df)
# df = pd.read_csv('C:/Users/王颖/Desktop/12.24日_商家代补.csv', sep=',', engine='python')
# print(df)

# 将新建的DataFrame储存为MySQL中的数据表，不储存index列(index=False)
# if_exists:
# 1.fail:如果表存在，啥也不做
# 2.replace:如果表存在，删了表，再建立一个新表，把数据插入
# 3.append:如果表存在，把数据插入，如果表不存在创建一个表！！
# 4.第一个参数要写入的dataframe, 第二个参数是 表名，第三个参数是数据库连接对象，第四个参数不写入行索引
# 5.第5个参数是判断表的存在情况

pd.io.sql.to_sql(df, '新签租房', con=engine, index=True, if_exists='replace')   # 索引没有存进去
# df.to_sql('example', con=engine,  if_exists='replace')这种形式也可以
print("Write to MySQL successfully!")