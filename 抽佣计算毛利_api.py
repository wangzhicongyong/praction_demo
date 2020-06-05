
"""
各城市抽佣计算毛利的api
"""
import pandas as pd

filename = 'C:/Users/xx/Desktop/20200120沙县.xlsx'
sheet_name = pd.ExcelFile(filename).sheet_names  # 读取表格里面几个工作表

for sheet in sheet_name:
    if sheet == '沙县':
        ji_shu01 = 4.45
        ji_shu02 = 0.025
        df01 = pd.read_excel(filename, sheet)  # 读取指定表格里面的数据
        # 修改指定的列名
        df01.rename(columns={'商业支持服务费费率%': '商业支持服务费费率'}, inplace=True)
        print(df01)
        # df01 = df01[df01['是否签署SD合作协议'] == '是']
        # 如果是SD商家，则把优惠申请书费率的值全部赋给商业支持服务费率
        # df01['商业支持服务费费率%'] = df01['优惠申请书费率']
        # print(df01)
        # 判断缺失值，用空格进行代替
        # df["VIN"] = df["VIN"].apply(lambda x: np.NaN if str(x).isspace() else x)
        for date, row in df01.T.iteritems():
            # print(date)  # 是行数 从0开始 获取的是行索引
            if row['是否签署SD合作协议'] == '是':
                # 替换单个单元格的值，切记，每一列的值必须是相同的数据类型
                # 直接在原有的dataframe上进行修改--得到修改后的新dataframe
                df01.at[date, '商业支持服务费费率'] = df01.at[date, '优惠申请书费率']
                # row['商业支持服务费费率%'] = row['优惠申请书费率']
        df02 = df01[df01['配送方式'] == '代理']
        df02.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 + 配送费 - 代理商补贴金额 - 订单数*{} - 原价交易额*{}'.format(ji_shu01, ji_shu02)
        df02.eval(param, inplace=True)
        # 该列保留三位小数
        df02['毛利金额'].round(decimals=3)
        df02 = df02[df02['毛利金额'] < 0]

        df03 = df01[df01['配送方式'] == '商家配送']
        df03.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 - 代理商补贴金额 - 原价交易额*{}'.format(ji_shu02)
        df03.eval(param, inplace=True)
        # 该列保留三位小数
        df03['毛利金额'].round(decimals=3)
        df03 = df03[df03['毛利金额'] < 0]
        # 将两个dataframe组合在一起
        df = pd.concat([df02, df03])
        # 设置指定的索引
        df.set_index(['日期'], inplace=True)
        print(df)
        url = 'C:/Users/王颖/Desktop/'
        df.to_excel(url + '沙县毛利.xlsx')

    if sheet == '桑植':
        ji_shu01 = 4.45
        ji_shu02 = 0.025
        df01 = pd.read_excel(filename, sheet)  # 读取指定表格里面的数据
        # 修改指定的列名
        df01.rename(columns={'商业支持服务费费率%': '商业支持服务费费率'}, inplace=True)
        print(df01)
        # df01 = df01[df01['是否签署SD合作协议'] == '是']
        # 如果是SD商家，则把优惠申请书费率的值全部赋给商业支持服务费率
        # df01['商业支持服务费费率%'] = df01['优惠申请书费率']
        # print(df01)
        # 判断缺失值，用空格进行代替
        # df["VIN"] = df["VIN"].apply(lambda x: np.NaN if str(x).isspace() else x)
        for date, row in df01.T.iteritems():
            # print(date)  # 是行数 从0开始 获取的是行索引
            if row['是否签署SD合作协议'] == '是':
                # 替换单个单元格的值，切记，每一列的值必须是相同的数据类型
                # 直接在原有的dataframe上进行修改--得到修改后的新dataframe
                df01.at[date, '商业支持服务费费率'] = df01.at[date, '优惠申请书费率']
                # row['商业支持服务费费率%'] = row['优惠申请书费率']
        df02 = df01[df01['配送方式'] == '代理']
        df02.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 + 配送费 - 代理商补贴金额 - 订单数*{} - 原价交易额*{}'.format(ji_shu01, ji_shu02)
        df02.eval(param, inplace=True)
        # 该列保留三位小数
        df02['毛利金额'].round(decimals=3)
        df02 = df02[df02['毛利金额'] < 0]

        df03 = df01[df01['配送方式'] == '商家配送']
        df03.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 - 代理商补贴金额 - 原价交易额*{}'.format(ji_shu02)
        df03.eval(param, inplace=True)
        # 该列保留三位小数
        df03['毛利金额'].round(decimals=3)
        df03 = df03[df03['毛利金额'] < 0]
        # 将两个dataframe组合在一起
        df = pd.concat([df02, df03])
        # 设置指定的索引
        df.set_index(['日期'], inplace=True)
        print(df)
        url = 'C:/Users/王颖/Desktop/'
        df.to_excel(url + '沙县毛利.xlsx')

    if sheet == '丹江口':
        ji_shu01 = 4.45
        ji_shu02 = 0.025
        df01 = pd.read_excel(filename, sheet)  # 读取指定表格里面的数据
        # 修改指定的列名
        df01.rename(columns={'商业支持服务费费率%': '商业支持服务费费率'}, inplace=True)
        print(df01)
        # df01 = df01[df01['是否签署SD合作协议'] == '是']
        # 如果是SD商家，则把优惠申请书费率的值全部赋给商业支持服务费率
        # df01['商业支持服务费费率%'] = df01['优惠申请书费率']
        # print(df01)
        # 判断缺失值，用空格进行代替
        # df["VIN"] = df["VIN"].apply(lambda x: np.NaN if str(x).isspace() else x)
        for date, row in df01.T.iteritems():
            # print(date)  # 是行数 从0开始 获取的是行索引
            if row['是否签署SD合作协议'] == '是':
                # 替换单个单元格的值，切记，每一列的值必须是相同的数据类型
                # 直接在原有的dataframe上进行修改--得到修改后的新dataframe
                df01.at[date, '商业支持服务费费率'] = df01.at[date, '优惠申请书费率']
                # row['商业支持服务费费率%'] = row['优惠申请书费率']
        df02 = df01[df01['配送方式'] == '代理']
        df02.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 + 配送费 - 代理商补贴金额 - 订单数*{} - 原价交易额*{}'.format(ji_shu01, ji_shu02)
        df02.eval(param, inplace=True)
        # 该列保留三位小数
        df02['毛利金额'].round(decimals=3)
        df02 = df02[df02['毛利金额'] < 0]

        df03 = df01[df01['配送方式'] == '商家配送']
        df03.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 - 代理商补贴金额 - 原价交易额*{}'.format(ji_shu02)
        df03.eval(param, inplace=True)
        # 该列保留三位小数
        df03['毛利金额'].round(decimals=3)
        df03 = df03[df03['毛利金额'] < 0]
        # 将两个dataframe组合在一起
        df = pd.concat([df02, df03])
        # 设置指定的索引
        df.set_index(['日期'], inplace=True)
        print(df)
        url = 'C:/Users/王颖/Desktop/'
        df.to_excel(url + '沙县毛利.xlsx')

    if sheet == '安陆':
        ji_shu01 = 4.45
        ji_shu02 = 0.025
        df01 = pd.read_excel(filename, sheet)  # 读取指定表格里面的数据
        # 修改指定的列名
        df01.rename(columns={'商业支持服务费费率%': '商业支持服务费费率'}, inplace=True)
        print(df01)
        # df01 = df01[df01['是否签署SD合作协议'] == '是']
        # 如果是SD商家，则把优惠申请书费率的值全部赋给商业支持服务费率
        # df01['商业支持服务费费率%'] = df01['优惠申请书费率']
        # print(df01)
        # 判断缺失值，用空格进行代替
        # df["VIN"] = df["VIN"].apply(lambda x: np.NaN if str(x).isspace() else x)
        for date, row in df01.T.iteritems():
            # print(date)  # 是行数 从0开始 获取的是行索引
            if row['是否签署SD合作协议'] == '是':
                # 替换单个单元格的值，切记，每一列的值必须是相同的数据类型
                # 直接在原有的dataframe上进行修改--得到修改后的新dataframe
                df01.at[date, '商业支持服务费费率'] = df01.at[date, '优惠申请书费率']
                # row['商业支持服务费费率%'] = row['优惠申请书费率']
        df02 = df01[df01['配送方式'] == '代理']
        df02.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 + 配送费 - 代理商补贴金额 - 订单数*{} - 原价交易额*{}'.format(ji_shu01, ji_shu02)
        df02.eval(param, inplace=True)
        # 该列保留三位小数
        df02['毛利金额'].round(decimals=3)
        df02 = df02[df02['毛利金额'] < 0]

        df03 = df01[df01['配送方式'] == '商家配送']
        df03.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 - 代理商补贴金额 - 原价交易额*{}'.format(ji_shu02)
        df03.eval(param, inplace=True)
        # 该列保留三位小数
        df03['毛利金额'].round(decimals=3)
        df03 = df03[df03['毛利金额'] < 0]
        # 将两个dataframe组合在一起
        df = pd.concat([df02, df03])
        # 设置指定的索引
        df.set_index(['日期'], inplace=True)
        print(df)
        url = 'C:/Users/王颖/Desktop/'
        df.to_excel(url + '沙县毛利.xlsx')

    if sheet == '孝昌':
        ji_shu01 = 4.45
        ji_shu02 = 0.025
        df01 = pd.read_excel(filename, sheet)  # 读取指定表格里面的数据
        # 修改指定的列名
        df01.rename(columns={'商业支持服务费费率%': '商业支持服务费费率'}, inplace=True)
        print(df01)
        # df01 = df01[df01['是否签署SD合作协议'] == '是']
        # 如果是SD商家，则把优惠申请书费率的值全部赋给商业支持服务费率
        # df01['商业支持服务费费率%'] = df01['优惠申请书费率']
        # print(df01)
        # 判断缺失值，用空格进行代替
        # df["VIN"] = df["VIN"].apply(lambda x: np.NaN if str(x).isspace() else x)
        for date, row in df01.T.iteritems():
            # print(date)  # 是行数 从0开始 获取的是行索引
            if row['是否签署SD合作协议'] == '是':
                # 替换单个单元格的值，切记，每一列的值必须是相同的数据类型
                # 直接在原有的dataframe上进行修改--得到修改后的新dataframe
                df01.at[date, '商业支持服务费费率'] = df01.at[date, '优惠申请书费率']
                # row['商业支持服务费费率%'] = row['优惠申请书费率']
        df02 = df01[df01['配送方式'] == '代理']
        df02.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 + 配送费 - 代理商补贴金额 - 订单数*{} - 原价交易额*{}'.format(ji_shu01, ji_shu02)
        df02.eval(param, inplace=True)
        # 该列保留三位小数
        df02['毛利金额'].round(decimals=3)
        df02 = df02[df02['毛利金额'] < 0]

        df03 = df01[df01['配送方式'] == '商家配送']
        df03.eval('抽佣金额 = 商品原价交易额 * 商业支持服务费费率/100', inplace=True)
        param = '毛利金额 = 抽佣金额 - 代理商补贴金额 - 原价交易额*{}'.format(ji_shu02)
        df03.eval(param, inplace=True)
        # 该列保留三位小数
        df03['毛利金额'].round(decimals=3)
        df03 = df03[df03['毛利金额'] < 0]
        # 将两个dataframe组合在一起
        df = pd.concat([df02, df03])
        # 设置指定的索引
        df.set_index(['日期'], inplace=True)
        print(df)
        url = 'C:/Users/王颖/Desktop/'
        df.to_excel(url + '沙县毛利.xlsx')
