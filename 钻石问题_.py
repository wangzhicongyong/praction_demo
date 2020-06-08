"""
10层电梯--每次只能拿一个
"""

# 排序问题
# def max_num(target):
#     for r in range(len(target)-1):
#         #p是移动的基准点--宝石
#         p = target[r]
#         for i in range(r,len(target)-1):
#             if p < target[i+1]:
#                 p = target[i+1]
#         return p

list = [1, 2, 3, 4, 5, 9, 6, 7, 34, 7, 8]
# max = list[0]
# for i in range(1,len(list)):
#     if max < list[i]:
#         max = list[i]
# print(max)
list = ['a', 'b', 'c']
a = list[1].replace('b', 'H')
print(list)