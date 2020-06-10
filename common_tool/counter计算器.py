
from collections import Counter

lists = ['a', 'a', 'b', 5, 6, 7, 5]
# 参数是可迭代对象
a = Counter(lists)  # Counter({'a': 2, 5: 2, 'b': 1, 6: 1, 7: 1})
print(a)
print(list(a))  # 有去重的效果

# 获取a中所有的键,返回的是一个对象,我们可以通过list来转化它
b = a.elements()   # 感觉有排序的作用
print(list(b))

# 前两个出现频率最高的元素已经他们的次数,返回的是元组列表
c = a.most_common(2)
print(c)

# 访问不存在的时候,默认返回0
a['zz']

# 更新被统计的对象,即原有的计数值与新增的相加,而不是替换
a.update("aa5bzz")

# 实现与原有的计数值相减,结果运行为0和负值
# a.subtrct("aaa5z")
