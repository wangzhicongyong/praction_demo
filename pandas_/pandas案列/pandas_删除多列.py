
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.arange(12).reshape(3, 4),
#            columns=['A', 'B', 'C', 'D'])
# print(df)
# x = [0, 2]
# df.drop(df.columns[x], axis=1, inplace=True)
# print(df)

import numpy as np
import pandas as pd
import time
import datetime

# 创建一个空的dateframe
data = pd.DataFrame({'A': ['2019-01-01 01:00:00', '2019-03-01 09:00:03', '2019-12-31 01:00:00'],
                     'B': ['2020-01-03 09:23:34', '2020-03-04 07:35:34', '2020-03-27 16:00:23'],
                     'C': ['2020-01-03 19:23:34', '2020-02-04 07:35:34', '2020-03-23 16:00:23']})
print(data)

print(pd.to_datetime(data['B']))

leadtime = (pd.to_datetime(data['B'])-pd.to_datetime(data['A'])).map(lambda x: x.days)
print(leadtime)
