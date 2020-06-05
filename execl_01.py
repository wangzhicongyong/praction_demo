"""
计算BD商家非异率
"""
import pandas as pd
from datetime import datetime
times = datetime.now().strftime('%Y-%m-%d')

filename = '22.xlsx'
sheet_name = pd.ExcelFile(filename).sheet_names
# print(sheet_name)   # ['沙县', '安陆', '丹江口']  返回值是列表
for sheet in sheet_name:
    if sheet == '沙县':
        df01 = pd.read_excel(filename, sheet)
        bd_name = df01['BD名称'].get_values()
        BD_name = list(bd_name)  # 直接转列表
        BD_name_list = set(BD_name)
        BD_name_list = list(BD_name_list)
        row_num = len(BD_name_list)
        city_name = list(df01['外卖组织结构'])[0]
        k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # BD名字的顺序是根据你提交的固定模板为标准，也可以随机排序，按模板一样，便于复制手动操作
        # BD_name_list = ['池美琴', '管尊槟', '刘慧思', '罗奋辉', '马万恒', '彭友焰', '邹杨']
        # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        city_list = [city_name]*row_num     # 生成多少个元素的列表
        list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        order_list = []
        bus_refuse_order = []
        bus_no_order = []
        n = 0
        for field in list01:
            n += 1
            for name in BD_name_list:
                    f = df01.loc[df01['BD名称'] == name][field].get_values()
                    f = list(f)
                    order_num = sum(f)
                    if n == 1:
                        order_list.append(order_num)
                    if n == 2:
                        bus_refuse_order.append(order_num)
                    if n == 3:
                        bus_no_order.append(order_num)
        print(order_list, bus_refuse_order, bus_no_order)
        d = {'城市': city_list, 'BD名称': BD_name_list, '订单数': order_list, '商家拒单订单数': bus_refuse_order,
             '商家不接单订单数': bus_no_order}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        df01 = pd.DataFrame(d)
        # refuse_lv = df['商家拒单订单数']/df['订单数']  整列整除
        # print(refuse_lv)
        df01.eval('拒单率 = 商家拒单订单数/订单数', inplace=True)    # 对dataframe进行操作生成新的列
        df01.eval('不接单率 = 商家不接单订单数/订单数', inplace=True)
        df01.eval('业务端非异率 = 拒单率+不接单率', inplace=True)  # 可以对新插入的列进行操作
        # 对数据的格式进行转换
        df01['拒单率'] = df01['拒单率'].apply(lambda x: format(x, '.2%'))
        df01['不接单率'] = df01['不接单率'].apply(lambda x: format(x, '.2%'))
        df01['业务端非异率'] = df01['业务端非异率'].apply(lambda x: format(x, '.2%'))
        df01.set_index(['城市'], inplace=True)
    if sheet == '安陆':
        df02 = pd.read_excel(filename, sheet)
        bd_name = df02['BD名称'].get_values()
        BD_name = list(bd_name)  # 直接转列表
        BD_name_list = set(BD_name)
        BD_name_list = list(BD_name_list)
        row_num = len(BD_name_list)
        city_name = list(df02['外卖组织结构'])[0]
        k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # BD_name_list = ['池美琴', '管尊槟', '刘慧思', '罗奋辉', '马万恒', '彭友焰', '邹杨']
        # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        city_list = [city_name] * row_num
        list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        order_list = []
        bus_refuse_order = []
        bus_no_order = []
        n = 0
        for field in list01:
            n += 1
            for name in BD_name_list:
                    f = df02.loc[df02['BD名称'] == name][field].get_values()
                    f = list(f)
                    order_num = sum(f)
                    if n == 1:
                        order_list.append(order_num)
                    if n == 2:
                        bus_refuse_order.append(order_num)
                    if n == 3:
                        bus_no_order.append(order_num)
                    print(name, order_num)
        print(order_list, bus_refuse_order, bus_no_order)
        d = {'城市': city_list, 'BD名称': BD_name_list, '订单数': order_list, '商家拒单订单数': bus_refuse_order,
             '商家不接单订单数': bus_no_order}
        df02 = pd.DataFrame(d)
        df02.eval('拒单率 = 商家拒单订单数/订单数', inplace=True)    # 对dataframe进行操作生成新的列
        df02.eval('不接单率 = 商家不接单订单数/订单数', inplace=True)
        df02.eval('业务端非异率 = 拒单率+不接单率', inplace=True)  # 可以对新插入的列进行操作
        df02['拒单率'] = df02['拒单率'].apply(lambda x: format(x, '.2%'))
        df02['不接单率'] = df02['不接单率'].apply(lambda x: format(x, '.2%'))
        df02['业务端非异率'] = df02['业务端非异率'].apply(lambda x: format(x, '.2%'))
        df02.set_index(['城市'], inplace=True)
    if sheet == '丹江口':
        df03 = pd.read_excel(filename, sheet)
        bd_name = df03['BD名称'].get_values()
        BD_name = list(bd_name)  # 直接转列表
        BD_name_list = set(BD_name)
        BD_name_list = list(BD_name_list)
        row_num = len(BD_name_list)
        city_name = list(df03['外卖组织结构'])[0]
        k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # BD_name_list = ['池美琴', '管尊槟', '刘慧思', '罗奋辉', '马万恒', '彭友焰', '邹杨']
        # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        city_list = [city_name] * row_num
        list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        order_list = []
        bus_refuse_order = []
        bus_no_order = []
        n = 0
        for field in list01:
            n += 1
            for name in BD_name_list:
                    f = df03.loc[df03['BD名称'] == name][field].get_values()
                    f = list(f)
                    order_num = sum(f)
                    if n == 1:
                        order_list.append(order_num)
                    if n == 2:
                        bus_refuse_order.append(order_num)
                    if n == 3:
                        bus_no_order.append(order_num)
                    print(name, order_num)
        print(order_list, bus_refuse_order, bus_no_order)
        d = {'城市': city_list, 'BD名称': BD_name_list, '订单数': order_list, '商家拒单订单数': bus_refuse_order,
             '商家不接单订单数': bus_no_order}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        df03 = pd.DataFrame(d)
        df03.eval('拒单率 = 商家拒单订单数/订单数', inplace=True)    # 对dataframe进行操作生成新的列
        df03.eval('不接单率 = 商家不接单订单数/订单数', inplace=True)
        df03.eval('业务端非异率 = 拒单率+不接单率', inplace=True)  # 可以对新插入的列进行操作
        df03['拒单率'] = df03['拒单率'].apply(lambda x: format(x, '.2%'))
        df03['不接单率'] = df03['不接单率'].apply(lambda x: format(x, '.2%'))
        df03['业务端非异率'] = df03['业务端非异率'].apply(lambda x: format(x, '.2%'))
        df03.set_index(['城市'], inplace=True)
    if sheet == '桑植':
        df04 = pd.read_excel(filename, sheet)
        bd_name = df04['BD名称'].get_values()
        BD_name = list(bd_name)  # 直接转列表
        BD_name_list = set(BD_name)
        BD_name_list = list(BD_name_list)
        row_num = len(BD_name_list)
        city_name = list(df04['外卖组织结构'])[0]
        k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # BD_name_list = ['池美琴', '管尊槟', '刘慧思', '罗奋辉', '马万恒', '彭友焰', '邹杨']
        # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        city_list = [city_name] * row_num
        list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        order_list = []
        bus_refuse_order = []
        bus_no_order = []
        n = 0
        for field in list01:
            n += 1
            for name in BD_name_list:
                    f = df04.loc[df04['BD名称'] == name][field].get_values()
                    f = list(f)
                    order_num = sum(f)
                    if n == 1:
                        order_list.append(order_num)
                    if n == 2:
                        bus_refuse_order.append(order_num)
                    if n == 3:
                        bus_no_order.append(order_num)
                    print(name, order_num)
        print(order_list, bus_refuse_order, bus_no_order)
        d = {'城市': city_list, 'BD名称': BD_name_list, '订单数': order_list, '商家拒单订单数': bus_refuse_order,
             '商家不接单订单数': bus_no_order}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        df04 = pd.DataFrame(d)
        df04.eval('拒单率 = 商家拒单订单数/订单数', inplace=True)    # 对dataframe进行操作生成新的列
        df04.eval('不接单率 = 商家不接单订单数/订单数', inplace=True)
        df04.eval('业务端非异率 = 拒单率+不接单率', inplace=True)  # 可以对新插入的列进行操作
        df04['拒单率'] = df04['拒单率'].apply(lambda x: format(x, '.2%'))
        df04['不接单率'] = df04['不接单率'].apply(lambda x: format(x, '.2%'))
        df04['业务端非异率'] = df04['业务端非异率'].apply(lambda x: format(x, '.2%'))
        df04.set_index(['城市'], inplace=True)
    if sheet == '孝昌':
        df05 = pd.read_excel(filename, sheet)
        bd_name = df05['BD名称'].get_values()
        BD_name = list(bd_name)  # 直接转列表
        BD_name_list = set(BD_name)
        BD_name_list = list(BD_name_list)
        row_num = len(BD_name_list)
        city_name = list(df05['外卖组织结构'])[0]
        k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # BD_name_list = ['池美琴', '管尊槟', '刘慧思', '罗奋辉', '马万恒', '彭友焰', '邹杨']
        # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        city_list = [city_name] * row_num
        list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        order_list = []
        bus_refuse_order = []
        bus_no_order = []
        n = 0
        for field in list01:
            n += 1
            for name in BD_name_list:
                    f = df05.loc[df05['BD名称'] == name][field].get_values()
                    f = list(f)
                    order_num = sum(f)
                    if n == 1:
                        order_list.append(order_num)
                    if n == 2:
                        bus_refuse_order.append(order_num)
                    if n == 3:
                        bus_no_order.append(order_num)
                    print(name, order_num)
        print(order_list, bus_refuse_order, bus_no_order)
        d = {'城市': city_list, 'BD名称': BD_name_list, '订单数': order_list, '商家拒单订单数': bus_refuse_order,
             '商家不接单订单数': bus_no_order}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        df05 = pd.DataFrame(d)
        df05.eval('拒单率 = 商家拒单订单数/订单数', inplace=True)    # 对dataframe进行操作生成新的列
        df05.eval('不接单率 = 商家不接单订单数/订单数', inplace=True)
        df05.eval('业务端非异率 = 拒单率+不接单率', inplace=True)  # 可以对新插入的列进行操作
        df05['拒单率'] = df05['拒单率'].apply(lambda x: format(x, '.2%'))
        df05['不接单率'] = df05['不接单率'].apply(lambda x: format(x, '.2%'))
        df05['业务端非异率'] = df05['业务端非异率'].apply(lambda x: format(x, '.2%'))
        df05.set_index(['城市'], inplace=True)

# 将多个dataframe数据写入同一个Excel的不同sheet中
url = 'C:/Users/王颖/Desktop/changzhoufeiniao_工作表/'
with pd.ExcelWriter(url+"BD商家非异率统计表.xlsx") as writer:
    df01.to_excel(writer, sheet_name='沙县')
    df02.to_excel(writer, sheet_name='安陆')
    df03.to_excel(writer, sheet_name='丹江口')
    df04.to_excel(writer, sheet_name='桑植')
    df05.to_excel(writer, sheet_name='孝昌')



