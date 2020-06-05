"""
计算BD商家非异率
"""
import pandas as pd
from datetime import datetime
times = datetime.now().strftime('%Y-%m-%d')

# filename = '22.xlsx'
filename = '工单记录.xlsx'
# sheet_name = ['沙县', '桑植', '安陆', '孝昌', '丹江口']
sheet_name = pd.ExcelFile(filename).sheet_names
# print(sheet_name)
# order_list01 = []
# bus_refuse_order01 = []
# bus_no_order01 = []
# city_list01 = []
# BD_name_list01 = []
for sheet in sheet_name:
    if sheet == '硚口店':
        df = pd.read_excel(filename, sheet)
        print(df)
        # bd_name = df01['BD名称'].get_values()
        # BD_name = list(bd_name)  # 直接转列表
        # BD_name_list = set(BD_name)
        # BD_name_list = list(BD_name_list)
        # row_num = len(BD_name_list)
        # city_name = list(df01['外卖组织结构'])[0]
        # k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # # BD名字的顺序是根据你提交的固定模板为标准，也可以随机排序，按模板一样，便于复制手动操作
        # # BD_name_list = ['池美琴', '管尊槟', '刘慧思', '罗奋辉', '马万恒', '彭友焰', '邹杨']
        # BD_name_list01.extend(BD_name_list)
        # # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        # city_list = [city_name]*row_num     # 生成多少个元素的列表
        # city_list01.extend(city_list)
        # list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        # # order_list01 = []
        # # bus_refuse_order01 = []
        # # bus_no_order01 = []
        # n = 0
        # for field in list01:
        #     n += 1
        #     for name in BD_name_list:
        #             f = df01.loc[df01['BD名称'] == name][field].get_values()
        #             f = list(f)
        #             order_num = sum(f)
        #             if n == 1:
        #                 order_list01.append(order_num)
        #             if n == 2:
        #                 bus_refuse_order01.append(order_num)
        #             if n == 3:
        #                 bus_no_order01.append(order_num)
    if sheet == '东西湖店':
        df = pd.read_excel(filename, sheet)
        print(df)
        # bd_name = df02['BD名称'].get_values()
        # BD_name = list(bd_name)  # 直接转列表
        # BD_name_list = set(BD_name)
        # BD_name_list = list(BD_name_list)
        # row_num = len(BD_name_list)
        # city_name = list(df02['外卖组织结构'])[0]
        # k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # # BD_name_list03 = ['陈梦蝶', '程博', '潘毅', '徐巧', '魏娟']
        # BD_name_list01.extend(BD_name_list)
        # # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        # city_list = [city_name] * row_num
        # city_list01.extend(city_list)
        # list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        # order_list03 = []
        # bus_refuse_order03 = []
        # bus_no_order03 = []
        # n = 0
        # for field in list01:
        #     n += 1
        #     for name in BD_name_list:
        #             f = df02.loc[df02['BD名称'] == name][field].get_values()
        #             f = list(f)
        #             order_num = sum(f)
        #             if n == 1:
        #                 order_list03.append(order_num)
        #             if n == 2:
        #                 bus_refuse_order03.append(order_num)
        #             if n == 3:
        #                 bus_no_order03.append(order_num)
        # order_list01.extend(order_list03)
        # bus_refuse_order01.extend(bus_refuse_order03)
        # bus_no_order01.extend(bus_no_order03)
    # if sheet == '丹江口':
    #     df03 = pd.read_excel(filename, sheet)
    #     pass
    #     bd_name = df03['BD名称'].get_values()
        # BD_name = list(bd_name)  # 直接转列表
        # BD_name_list = set(BD_name)
        # BD_name_list = list(BD_name_list)
        # row_num = len(BD_name_list)
        # city_name = list(df03['外卖组织结构'])[0]
        # k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # # BD_name_list05 = ['陈巧英', '陈忠玉', '付安坤', '郭君', '宋娟', '伍亚男', '黄平']
        # BD_name_list01.extend(BD_name_list)
        # # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        # city_list = [city_name] * row_num
        # city_list01.extend(city_list)
        # list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        # order_list05 = []
        # bus_refuse_order05 = []
        # bus_no_order05 = []
        # n = 0
        # for field in list01:
        #     n += 1
        #     for name in BD_name_list:
        #             f = df03.loc[df03['BD名称'] == name][field].get_values()
        #             f = list(f)
        #             order_num = sum(f)
        #             if n == 1:
        #                 order_list05.append(order_num)
        #             if n == 2:
        #                 bus_refuse_order05.append(order_num)
        #             if n == 3:
        #                 bus_no_order05.append(order_num)
        # order_list01.extend(order_list05)
        # bus_refuse_order01.extend(bus_refuse_order05)
        # bus_no_order01.extend(bus_no_order05)
    # if sheet == '桑植':
    #     df04 = pd.read_excel(filename, sheet)
    #     pass
        # bd_name = df04['BD名称'].get_values()
        # BD_name = list(bd_name)  # 直接转列表
        # BD_name_list = set(BD_name)
        # BD_name_list = list(BD_name_list)
        # row_num = len(BD_name_list)
        # city_name = list(df04['外卖组织结构'])[0]
        # k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # # BD_name_list02 = ['黎朗', '吴正浩', '张晓燕']
        # BD_name_list01.extend(BD_name_list)
        # # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        # city_list = [city_name] * row_num
        # city_list01.extend(city_list)
        # list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        # order_list02 = []   # 列表的顺序是以统计模板BD的名字循序和城市的循序来定
        # bus_refuse_order02 = []
        # bus_no_order02 = []
        # n = 0
        # for field in list01:
        #     n += 1
        #     for name in BD_name_list:
        #             f = df04.loc[df04['BD名称'] == name][field].get_values()
        #             f = list(f)
        #             order_num = sum(f)
        #             if n == 1:
        #                 order_list02.append(order_num)
        #             if n == 2:
        #                 bus_refuse_order02.append(order_num)
        #             if n == 3:
        #                 bus_no_order02.append(order_num)
        #             print(name, order_num)
        # order_list01.extend(order_list02)
        # bus_refuse_order01.extend(bus_refuse_order02)
        # bus_no_order01.extend(bus_no_order02)
    # if sheet == '孝昌':
    #     df05 = pd.read_excel(filename, sheet)
    #     pass
        # bd_name = df05['BD名称'].get_values()
        # BD_name = list(bd_name)  # 直接转列表
        # BD_name_list = set(BD_name)
        # BD_name_list = list(BD_name_list)
        # row_num = len(BD_name_list)
        # city_name = list(df05['外卖组织结构'])[0]
        # k_titile_list = ['拒单率', '不接单率', '业务端非异率']
        # # BD_name_list04 = ['丁鹏', '樊迅', '冯超超', '李艳秋', '余洋', '袁小玲']
        # BD_name_list01.extend(BD_name_list)
        # # city_list = ['沙县', '沙县', '沙县', '沙县', '沙县', '沙县', '沙县']
        # city_list = [city_name] * row_num
        # city_list01.extend(city_list)
        # list01 = ['订单数', '商家拒单订单数', '商家不接单订单数']
        # order_list04 = []
        # bus_refuse_order04 = []
        # bus_no_order04 = []
        # n = 0
        # for field in list01:
        #     n += 1
        #     for name in BD_name_list:
        #             f = df05.loc[df05['BD名称'] == name][field].get_values()
        #             f = list(f)
        #             order_num = sum(f)
        #             if n == 1:
        #                 order_list04.append(order_num)
        #             if n == 2:
        #                 bus_refuse_order04.append(order_num)
        #             if n == 3:
        #                 bus_no_order04.append(order_num)
        # order_list01.extend(order_list04)
        # bus_refuse_order01.extend(bus_refuse_order04)
        # bus_no_order01.extend(bus_no_order04)
    # print(len(order_list01))
    # print(len(bus_refuse_order01))
    # print(len(bus_no_order01))
    # print(city_list01)
# else:
#     d = {'外卖组织结构': city_list01, 'BD名称': BD_name_list01, '订单数': order_list01, '商家拒单订单数': bus_refuse_order01,
#          '商家不接单订单数': bus_no_order01}
#     labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     df05 = pd.DataFrame(d)
#     df05.eval('拒单率 = 商家拒单订单数/订单数', inplace=True)    # 对dataframe进行操作生成新的列
#     df05.eval('不接单率 = 商家不接单订单数/订单数', inplace=True)
#     df05.eval('业务端非异率 = 拒单率+不接单率', inplace=True)  # 可以对新插入的列进行操作
#
#     df05['拒单率'] = df05['拒单率'].apply(lambda x: format(x, '.2%'))
#     df05['不接单率'] = df05['不接单率'].apply(lambda x: format(x, '.2%'))
#     df05['业务端非异率'] = df05['业务端非异率'].apply(lambda x: format(x, '.2%'))
#     df05.set_index(['外卖组织结构'], inplace=True)
#     url = 'C:/Users/王颖/Desktop/'
#     df05.to_excel(url+'BD.xlsx')

# 将多个dataframe数据写入同一个Excel的不同sheet中
# url = 'C:/Users/王颖/Desktop/changzhoufeiniao_工作表/'
# with pd.ExcelWriter(url+"BD商家非异率统计表.xlsx") as writer:
#     df01.to_excel(writer, sheet_name='沙县')
#     df02.to_excel(writer, sheet_name='安陆')
#     df03.to_excel(writer, sheet_name='丹江口')
#     df04.to_excel(writer, sheet_name='桑植')
#     df05.to_excel(writer, sheet_name='孝昌')