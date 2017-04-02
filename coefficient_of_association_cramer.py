# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

#　対象データ
data = pd.DataFrame(
    {'TOKYO': ['sunny', 'sunny', 'rainy', 'sunny', 'snowy', 'cloudy', 'sunny',
                 'sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny',
                 'cloudy', 'sunny', 'sunny', 'sunny', 'sunny', 'snowy', 'cloudy',
                 'cloudy', 'sunny', 'snowy', 'sunny', 'sunny', 'sunny', 'sunny',
],
     'OSAKA': ['sunny', 'sunny', 'sunny', 'sunny', 'rainy', 'cloudy', 'cloudy',
               'sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny',
               'cloudy', 'rainy', 'sunny', 'sunny', 'sunny', 'rainy', 'cloudy',
               'sunny', 'sunny', 'rainy', 'sunny', 'sunny', 'sunny', 'sunny',
               ]})

def correlation_coefficient_cramer(x, y):
    table = np.array(pd.crosstab(x, y)).astype(np.float32)
    n = table.sum()
    colsum = table.sum(axis=0)
    rowsum = table.sum(axis=1)
    expect = np.outer(rowsum, colsum) / n
    chisq = np.sum((table - expect) ** 2 / expect)
    print(u"クラメールの連関係数："+str(np.sqrt(chisq / (n * (np.min(table.shape) - 1)))))

if __name__ == "__main__":

    correlation_coefficient_cramer(data['TOKYO'], data['OSAKA'])

