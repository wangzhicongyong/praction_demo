
import pandas as pd
# pandas识别的日期字符串格式
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01',
                   '2011/05/01 01:01:01', '01 Jun 2011'])
# to_datetime() 转换日期数据类型
dates = pd.to_datetime(dates)
print(dates, dates.dtype, type(dates))

a = pd.to_datetime('1970-01-01')
print(a)

# datetime类型数据支持日期运算
delta = dates - pd.to_datetime('1970-01-01')
# 获取天数数值
print(delta.dt.days)

# 以日为频率
datelist = pd.date_range('2019/08/21', periods=5)
print(datelist)

# 以月为频率
datelist = pd.date_range('2019/08/21', periods=5, freq='M')
print(datelist)

# 构建某个区间的时间序列
start = pd.datetime(2017, 11, 1)
end = pd.datetime(2017, 11, 5)
dates = pd.date_range(start, end)
print(dates)
# DatetimeIndex(['2017-11-01', '2017-11-02', '2017-11-03', '2017-11-04',
               # '2017-11-05'],
              # dtype='datetime64[ns]', freq='D')