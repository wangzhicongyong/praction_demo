import numpy as np

ary = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
])
# 观察维度，size，len的区别
print(ary)
print(ary.shape, ary.size, len(ary))
# (2, 4) 8 2

ary01 = np.array([1, 2])
print(ary01.shape, ary01.size, len(ary01))
# (2,) 2 2

# 这是取所有行，第2列的值
print(ary[:, 2])  # [3 7]
print(ary[1, 1])  # 6


# 可以判断一个数是否在数组里面
ary02 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
], dtype=bool)

# 求的是维度数
print(ary02.ndim)
equal_ten = (ary02 == 10)
print(equal_ten)