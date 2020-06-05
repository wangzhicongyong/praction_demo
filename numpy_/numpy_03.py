import numpy as np
ary = np.array([1, 2, 3, 4, 5, 6])
print(type(ary), ary, ary.dtype)


# ary.shape 矩阵的维度
import numpy as np
ary = np.array([1, 2, 3, 4, 5, 6])
print(type(ary), ary, ary.shape)
#二维数组
ary = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(type(ary), ary, ary.shape)

import numpy as np
ary = np.array([1, 2, 3, 4, 5, 6])
print(type(ary), ary, ary.dtype)
# <class 'numpy.ndarray'> [1 2 3 4 5 6] (6,)

#转换ary元素的类型
b = ary.astype(float)
print(type(b), b, b.dtype)
#转换ary元素的类型
c = ary.astype(str)
print(type(c), c, c.dtype)

#<class 'numpy.ndarray'> [[ 1  2  3  4]
 # [ 5  6  7  8]
 # [ 9 10 11 12]] (3, 4)