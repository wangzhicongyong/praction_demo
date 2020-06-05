
import numpy as np
a = np.array([
              [[1, 2], [3, 4]],
              [[5, 6], [7, 8]],
              ])
# 里面的元素是一个列表
print(a, a.shape)
print(a[0])
print(a[0][0])
print(a[0][0][0])  # 1
print(a[0, 0, 0])  # 1
# 第一个循环取维度，也就是几行
for i in range(a.shape[0]):
    # 第二个循环是取是定位列表
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            print(a[i, j, k])


import numpy as np
a = np.array([
              [[1, 2, 3], [3, 4, 5]],
              [[5, 6], [7, 8]],
              ])
# 里面的元素是一个列表
print(a, a.shape)
print(a[0])
print(a[0][0])