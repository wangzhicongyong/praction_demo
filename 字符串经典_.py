
"""
给定一个text字符串和一个短字符串key,从text中找出第一次出现key字符串以及它出现的下标
"""
# 暴力匹配法 每次切取相同的子串进行对比，不是，则把子串向后推一位

def get_str(key, text):
    n = 0
    key_length = len(key)
    text_length = len(text)
    k_list = []
    t_list = []
    for k_str in key:
        k_list.append(k_str)
    while True:
        a = text[n:n+key_length]
        for t_str in a:
            t_list.append(t_str)
        if k_list == t_list:
            return n
        else:
            t_list.clear()  # 清空列表
            n = n + 1
            if n + key_length > text_length:
                print('该长串中不存在这个子串')
                return False

if __name__=="__main__":
    key = 'akje'
    text = 'akghjjakja'
    re = get_str(key, text)
    print(re)


