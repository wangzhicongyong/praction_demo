
"""
计算各城市商家运营数据情况
"""
import pandas as pd
from datetime import datetime
times = datetime.now().strftime('%Y-%m-%d')

filename = '沙县各商家运营数据.xlsx'
sheet_name = pd.ExcelFile(filename).sheet_names  # print(sheet_name)   # ['沙县', '安陆', '丹江口']  返回值是列表
for sheet in sheet_name:
    if sheet == '12月':
        gmv = 2257444.8
        order = 55475
        agent_money = 219801.25
        different_rate = 0.0099
        df01 = pd.read_excel(filename, sheet)
        # df[['col2', 'col3']] = df[['col2', 'col3']].apply(pd.to_numeric)
        # 将百分数转化为小数
        # df01 = df01.where(df01.notnull(), 0)  # 把所有为空的列的值改为None
        df01.ix[df01['非顾客原因异常订单率'] == '-', '非顾客原因异常订单率'] = 0  # 刷选
        df01['非顾客原因异常订单率'] = df01['非顾客原因异常订单率'].str.strip('%').astype(float) / 100
        df01 = df01.drop(['是否有双证'], axis=1)  # 删除列
        df01 = df01.drop(['是否签署SD合作协议'], axis=1)  # 删除列
        df01 = df01.drop(['一级品类'], axis=1)  # 删除列
        df01 = df01.drop(['二级品类'], axis=1)  # 删除列
        df01 = df01.drop(['代理商名称'], axis=1)  # 删除列
        df01 = df01.drop(['商家ID'], axis=1)  # 删除列
        df01 = df01.drop(['配送方式'], axis=1)  # 删除列
        df01 = df01.drop(['实际支付交易额'], axis=1)  # 删除列
        # df01 = df01.drop(['配送方式'], axis=1)  # 删除列
        df01['原价交易额贡献占比'] = 0  # 可以增加新的列
        df01['原价交易额贡献占比'] = df01.apply(lambda x: df01['原价交易额'] / gmv)
        df01['原价交易额贡献占比'] = df01['原价交易额贡献占比'].apply(lambda x: format(x, '.2%'))
        df01['订单数贡献占比'] = 0
        df01['订单数贡献占比'] = df01.apply(lambda x: df01['订单数'] / order)
        df01['订单数贡献占比'] = df01['订单数贡献占比'].apply(lambda x: format(x, '.2%'))
        df01['代补金额贡献占比'] = 0
        df01['代补金额贡献占比'] = df01.apply(lambda x: df01['代理商补贴金额'] / agent_money)
        df01['代补金额贡献占比'] = df01['代补金额贡献占比'].apply(lambda x: format(x, '.2%'))
        df01['非异贡献占比'] = 0
        df01['非异贡献占比'] = df01.apply(lambda x: df01['非顾客原因异常订单率'] / different_rate)
        df01['非异贡献占比'] = df01['非异贡献占比'].apply(lambda x: format(x, '.2%'))
        # 排序  一定要记得先将数据转化成 int类型
        # df01.sort_values(["原价交易额贡献占比", "订单数贡献占比", '代补金额贡献占比', '非异贡献占比'], ascending=False)
        df01["订单数"] = df01["订单数"].astype("int")  # 强制转化类型
        # inplace表示再排序的时候是否生成一个新的dataframe 结构
        df01.sort_values(["原价交易额贡献占比"], inplace=True, ascending=False)
        df01 = df01.head(30)
        df01.set_index(['外卖组织结构'], inplace=True)
        # url = 'C:/Users/王颖/Desktop/'
        # df01.to_excel(url + '沙县11月各商家数据明细.xlsx')
    if sheet == '11月':
        gmv = 2160776.78
        order = 54250
        agent_money = 182178.55
        different_rate = 0.0107
        df02 = pd.read_excel(filename, sheet)
        # df[['col2', 'col3']] = df[['col2', 'col3']].apply(pd.to_numeric)
        # 将百分数转化为小数
        # df01 = df01.where(df01.notnull(), 0)  # 把所有为空的列的值改为None
        df02.ix[df02['非顾客原因异常订单率'] == '-', '非顾客原因异常订单率'] = 0  # 刷选
        df02['非顾客原因异常订单率'] = df02['非顾客原因异常订单率'].str.strip('%').astype(float) / 100
        df02 = df02.drop(['是否有双证'], axis=1)  # 删除列
        df02 = df02.drop(['是否签署SD合作协议'], axis=1)  # 删除列
        df02 = df02.drop(['一级品类'], axis=1)  # 删除列
        df02 = df02.drop(['二级品类'], axis=1)  # 删除列
        df02 = df02.drop(['代理商名称'], axis=1)  # 删除列
        df02 = df02.drop(['商家ID'], axis=1)  # 删除列
        df02 = df02.drop(['配送方式'], axis=1)  # 删除列
        df02 = df02.drop(['实际支付交易额'], axis=1)  # 删除列
        # df01 = df01.drop(['配送方式'], axis=1)  # 删除列
        df02['原价交易额贡献占比'] = 0  # 可以增加新的列
        df02['原价交易额贡献占比'] = df02.apply(lambda x: df02['原价交易额']/gmv)
        df02['原价交易额贡献占比'] = df02['原价交易额贡献占比'].apply(lambda x: format(x, '.2%'))
        df02['订单数贡献占比'] = 0
        df02['订单数贡献占比'] = df02.apply(lambda x: df02['订单数'] / order)
        df02['订单数贡献占比'] = df02['订单数贡献占比'].apply(lambda x: format(x, '.2%'))
        df02['代补金额贡献占比'] = 0
        df02['代补金额贡献占比'] = df02.apply(lambda x: df02['代理商补贴金额'] / agent_money)
        df02['代补金额贡献占比'] = df02['代补金额贡献占比'].apply(lambda x: format(x, '.2%'))
        df02['非异贡献占比'] = 0
        df02['非异贡献占比'] = df02.apply(lambda x: df02['非顾客原因异常订单率'] / different_rate)
        df02['非异贡献占比'] = df02['非异贡献占比'].apply(lambda x: format(x, '.2%'))
        # 排序  一定要记得先将数据转化成 int类型
        # df01.sort_values(["原价交易额贡献占比", "订单数贡献占比", '代补金额贡献占比', '非异贡献占比'], ascending=False)
        df02["订单数"] = df02["订单数"].astype("int")   # 强制转化类型
        # inplace表示再排序的时候是否生成一个新的dataframe 结构
        df02.sort_values(["原价交易额贡献占比"], inplace=True, ascending=False)
        df02 = df02.head(30)
        df02.set_index(['外卖组织结构'], inplace=True)
        # url = 'C:/Users/王颖/Desktop/'
        # df01.to_excel(url + '沙县11月各商家数据明细.xlsx')
    if sheet == '10月':
        gmv = 2300995.2
        order = 56908
        agent_money = 191680.21
        different_rate = 0.0094
        df03 = pd.read_excel(filename, sheet)
        # df[['col2', 'col3']] = df[['col2', 'col3']].apply(pd.to_numeric)
        # 将百分数转化为小数
        # df01 = df01.where(df01.notnull(), 0)  # 把所有为空的列的值改为None
        df03.ix[df03['非顾客原因异常订单率'] == '-', '非顾客原因异常订单率'] = 0  # 刷选
        df03['非顾客原因异常订单率'] = df03['非顾客原因异常订单率'].str.strip('%').astype(float) / 100
        df03 = df03.drop(['是否有双证'], axis=1)  # 删除列
        df03 = df03.drop(['是否签署SD合作协议'], axis=1)  # 删除列
        df03 = df03.drop(['一级品类'], axis=1)  # 删除列
        df03 = df03.drop(['二级品类'], axis=1)  # 删除列
        df03 = df03.drop(['代理商名称'], axis=1)  # 删除列
        df03 = df03.drop(['商家ID'], axis=1)  # 删除列
        df03 = df03.drop(['配送方式'], axis=1)  # 删除列
        df03 = df03.drop(['实际支付交易额'], axis=1)  # 删除列
        # df01 = df01.drop(['配送方式'], axis=1)  # 删除列
        df03['原价交易额贡献占比'] = 0  # 可以增加新的列
        df03['原价交易额贡献占比'] = df03.apply(lambda x: df03['原价交易额'] / gmv)
        df03['原价交易额贡献占比'] = df03['原价交易额贡献占比'].apply(lambda x: format(x, '.2%'))
        df03['订单数贡献占比'] = 0
        df03['订单数贡献占比'] = df03.apply(lambda x: df03['订单数'] / order)
        df03['订单数贡献占比'] = df03['订单数贡献占比'].apply(lambda x: format(x, '.2%'))
        df03['代补金额贡献占比'] = 0
        df03['代补金额贡献占比'] = df03.apply(lambda x: df03['代理商补贴金额'] / agent_money)
        df03['代补金额贡献占比'] = df03['代补金额贡献占比'].apply(lambda x: format(x, '.2%'))
        df03['非异贡献占比'] = 0
        df03['非异贡献占比'] = df03.apply(lambda x: df03['非顾客原因异常订单率'] / different_rate)
        df03['非异贡献占比'] = df03['非异贡献占比'].apply(lambda x: format(x, '.2%'))
        # 排序  一定要记得先将数据转化成 int类型
        # df01.sort_values(["原价交易额贡献占比", "订单数贡献占比", '代补金额贡献占比', '非异贡献占比'], ascending=False)
        df03["订单数"] = df03["订单数"].astype("int")  # 强制转化类型
        # inplace表示再排序的时候是否生成一个新的dataframe 结构
        df03.sort_values(["原价交易额贡献占比"], inplace=True, ascending=False)
        df03 = df03.head(30)
        df03.set_index(['外卖组织结构'], inplace=True)
        # url = 'C:/Users/王颖/Desktop/'
        # df01.to_excel(url + '沙县11月各商家数据明细.xlsx')
    if sheet == '9月':
        gmv = 2055899.15
        order = 50911
        agent_money = 174015.28
        different_rate = 0.0132
        df04 = pd.read_excel(filename, sheet)
        # df[['col2', 'col3']] = df[['col2', 'col3']].apply(pd.to_numeric)
        # 将百分数转化为小数
        # df01 = df01.where(df01.notnull(), 0)  # 把所有为空的列的值改为None
        df04.ix[df04['非顾客原因异常订单率'] == '-', '非顾客原因异常订单率'] = 0  # 刷选
        df04['非顾客原因异常订单率'] = df04['非顾客原因异常订单率'].str.strip('%').astype(float) / 100
        df04 = df04.drop(['是否有双证'], axis=1)  # 删除列
        df04 = df04.drop(['是否签署SD合作协议'], axis=1)  # 删除列
        df04 = df04.drop(['一级品类'], axis=1)  # 删除列
        df04 = df04.drop(['二级品类'], axis=1)  # 删除列
        df04 = df04.drop(['代理商名称'], axis=1)  # 删除列
        df04 = df04.drop(['商家ID'], axis=1)  # 删除列
        df04 = df04.drop(['配送方式'], axis=1)  # 删除列
        df04 = df04.drop(['实际支付交易额'], axis=1)  # 删除列
        # df01 = df01.drop(['配送方式'], axis=1)  # 删除列
        df04['原价交易额贡献占比'] = 0  # 可以增加新的列
        df04['原价交易额贡献占比'] = df04.apply(lambda x: df04['原价交易额'] / gmv)
        df04['原价交易额贡献占比'] = df04['原价交易额贡献占比'].apply(lambda x: format(x, '.2%'))
        df04['订单数贡献占比'] = 0
        df04['订单数贡献占比'] = df04.apply(lambda x: df04['订单数'] / order)
        df04['订单数贡献占比'] = df04['订单数贡献占比'].apply(lambda x: format(x, '.2%'))
        df04['代补金额贡献占比'] = 0
        df04['代补金额贡献占比'] = df04.apply(lambda x: df04['代理商补贴金额'] / agent_money)
        df04['代补金额贡献占比'] = df04['代补金额贡献占比'].apply(lambda x: format(x, '.2%'))
        df04['非异贡献占比'] = 0
        df04['非异贡献占比'] = df04.apply(lambda x: df04['非顾客原因异常订单率'] / different_rate)
        df04['非异贡献占比'] = df04['非异贡献占比'].apply(lambda x: format(x, '.2%'))
        # 排序  一定要记得先将数据转化成 int类型
        # df01.sort_values(["原价交易额贡献占比", "订单数贡献占比", '代补金额贡献占比', '非异贡献占比'], ascending=False)
        df04["订单数"] = df04["订单数"].astype("int")  # 强制转化类型
        # inplace表示再排序的时候是否生成一个新的dataframe 结构
        df04.sort_values(["原价交易额贡献占比"], inplace=True, ascending=False)
        df04 = df04.head(30)
        df04.set_index(['外卖组织结构'], inplace=True)
        # url = 'C:/Users/王颖/Desktop/'
        # df01.to_excel(url + '沙县11月各商家数据明细.xlsx')
    if sheet == '8月':
        gmv = 2692068.51
        order = 65329
        agent_money = 219326.55
        different_rate = 0.0156
        df05 = pd.read_excel(filename, sheet)
        # df[['col2', 'col3']] = df[['col2', 'col3']].apply(pd.to_numeric)
        # 将百分数转化为小数
        # df01 = df01.where(df01.notnull(), 0)  # 把所有为空的列的值改为None
        df05.ix[df05['非顾客原因异常订单率'] == '-', '非顾客原因异常订单率'] = 0  # 刷选
        df05['非顾客原因异常订单率'] = df05['非顾客原因异常订单率'].str.strip('%').astype(float) / 100
        df05 = df05.drop(['是否有双证'], axis=1)  # 删除列
        df05 = df05.drop(['是否签署SD合作协议'], axis=1)  # 删除列
        df05 = df05.drop(['一级品类'], axis=1)  # 删除列
        df05 = df05.drop(['二级品类'], axis=1)  # 删除列
        df05 = df05.drop(['代理商名称'], axis=1)  # 删除列
        df05 = df05.drop(['商家ID'], axis=1)  # 删除列
        df05 = df05.drop(['配送方式'], axis=1)  # 删除列
        df05 = df05.drop(['实际支付交易额'], axis=1)  # 删除列
        # df01 = df01.drop(['配送方式'], axis=1)  # 删除列
        df05['原价交易额贡献占比'] = 0  # 可以增加新的列
        df05['原价交易额贡献占比'] = df05.apply(lambda x: df05['原价交易额'] / gmv)
        df05['原价交易额贡献占比'] = df05['原价交易额贡献占比'].apply(lambda x: format(x, '.2%'))
        df05['订单数贡献占比'] = 0
        df05['订单数贡献占比'] = df05.apply(lambda x: df05['订单数'] / order)
        df05['订单数贡献占比'] = df05['订单数贡献占比'].apply(lambda x: format(x, '.2%'))
        df05['代补金额贡献占比'] = 0
        df05['代补金额贡献占比'] = df05.apply(lambda x: df05['代理商补贴金额'] / agent_money)
        df05['代补金额贡献占比'] = df05['代补金额贡献占比'].apply(lambda x: format(x, '.2%'))
        df05['非异贡献占比'] = 0
        df05['非异贡献占比'] = df05.apply(lambda x: df05['非顾客原因异常订单率'] / different_rate)
        df05['非异贡献占比'] = df05['非异贡献占比'].apply(lambda x: format(x, '.2%'))
        # 排序  一定要记得先将数据转化成 int类型
        # df01.sort_values(["原价交易额贡献占比", "订单数贡献占比", '代补金额贡献占比', '非异贡献占比'], ascending=False)
        df05["订单数"] = df05["订单数"].astype("int")  # 强制转化类型
        # inplace表示再排序的时候是否生成一个新的dataframe 结构
        df05.sort_values(["原价交易额贡献占比"], inplace=True, ascending=False)
        df05 = df05.head(30)
        df05.set_index(['外卖组织结构'], inplace=True)
        # url = 'C:/Users/王颖/Desktop/'
        # df01.to_excel(url + '沙县11月各商家数据明细.xlsx')
    if sheet == '7月':
        gmv = 2627850.44
        order = 63877
        agent_money = 221700.17
        different_rate = 0.0184
        df06 = pd.read_excel(filename, sheet)
        # df[['col2', 'col3']] = df[['col2', 'col3']].apply(pd.to_numeric)
        # 将百分数转化为小数
        # df01 = df01.where(df01.notnull(), 0)  # 把所有为空的列的值改为None
        df06.ix[df06['非顾客原因异常订单率'] == '-', '非顾客原因异常订单率'] = 0  # 刷选
        df06['非顾客原因异常订单率'] = df06['非顾客原因异常订单率'].str.strip('%').astype(float) / 100
        df06 = df06.drop(['是否有双证'], axis=1)  # 删除列
        df06 = df06.drop(['是否签署SD合作协议'], axis=1)  # 删除列
        df06 = df06.drop(['一级品类'], axis=1)  # 删除列
        df06 = df06.drop(['二级品类'], axis=1)  # 删除列
        df06 = df06.drop(['代理商名称'], axis=1)  # 删除列
        df06 = df06.drop(['商家ID'], axis=1)  # 删除列
        df06 = df06.drop(['配送方式'], axis=1)  # 删除列
        df06 = df06.drop(['实际支付交易额'], axis=1)  # 删除列
        # df01 = df01.drop(['配送方式'], axis=1)  # 删除列
        df06['原价交易额贡献占比'] = 0  # 可以增加新的列
        df06['原价交易额贡献占比'] = df06.apply(lambda x: df06['原价交易额'] / gmv)
        df06['原价交易额贡献占比'] = df06['原价交易额贡献占比'].apply(lambda x: format(x, '.2%'))
        df06['订单数贡献占比'] = 0
        df06['订单数贡献占比'] = df06.apply(lambda x: df06['订单数'] / order)
        df06['订单数贡献占比'] = df06['订单数贡献占比'].apply(lambda x: format(x, '.2%'))
        df06['代补金额贡献占比'] = 0
        df06['代补金额贡献占比'] = df06.apply(lambda x: df06['代理商补贴金额'] / agent_money)
        df06['代补金额贡献占比'] = df06['代补金额贡献占比'].apply(lambda x: format(x, '.2%'))
        df06['非异贡献占比'] = 0
        df06['非异贡献占比'] = df06.apply(lambda x: df06['非顾客原因异常订单率'] / different_rate)
        df06['非异贡献占比'] = df06['非异贡献占比'].apply(lambda x: format(x, '.2%'))
        # 排序  一定要记得先将数据转化成 int类型
        # df01.sort_values(["原价交易额贡献占比", "订单数贡献占比", '代补金额贡献占比', '非异贡献占比'], ascending=False)
        df06["订单数"] = df06["订单数"].astype("int")  # 强制转化类型
        # inplace表示再排序的时候是否生成一个新的dataframe 结构
        df06.sort_values(["原价交易额贡献占比"], inplace=True, ascending=False)
        df06 = df06.head(30)
        df06.set_index(['外卖组织结构'], inplace=True)
        # url = 'C:/Users/王颖/Desktop/'
        # df01.to_excel(url + '沙县11月各商家数据明细.xlsx')

# 将多个dataframe数据写入同一个Excel的不同sheet中
url = 'C:/Users/王颖/Desktop/'
with pd.ExcelWriter(url+"沙县各商家运营情况.xlsx") as writer:
    print(df01)
    df01.to_excel(writer, sheet_name='沙县12月')
    df02.to_excel(writer, sheet_name='沙县11月')
    df03.to_excel(writer, sheet_name='沙县10月')
    df04.to_excel(writer, sheet_name='沙县9月')
    df05.to_excel(writer, sheet_name='沙县8月')
    df06.to_excel(writer, sheet_name='沙县7月')



