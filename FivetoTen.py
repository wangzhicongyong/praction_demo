
"""
5进制转10进制
"""
# 十进制数转换为二进制数时，由于整数和小数的转换方法不同，所以先将十进制数的整数部分和小数部分分别转换后，再加以合并
# 输入两个五进制的数,转化成10进制--进行加和--然后再转5进制
# 输入一个五进制的数值

def fiveToTen(value):
    """5进制转10进制"""
    value = str(value)
    n = 0
    result = 0
    for i in str(value):
        n = n+1
        result += int(i)*5**int((len(value)-n))
    return result

def tenToFive(num01, num02):
    """10进制转5进制"""
    value1 = fiveToTen(num01)
    value2 = fiveToTen(num02)
    result = value1 + value2
    list01 = []
    while True:
        # 取余
        a = result % 5
        # 取整，整数接着除5
        b = result // 5
        list01.append(str(a))
        if a < 5 and b < 5:
            list01.append(str(b))
            # 倒转一下
            return "".join(list01[::-1])
        result = b


if __name__ == "__main__":
    re = tenToFive(120, 120)
    print(re)
    re = fiveToTen(240)
    print(re)