# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import zscore

# テストデータを生成（外れ値：10000）
data = np.array([150, 20, 10000, 10, 300])

def z_score_normalize_data(data):
    normalization_data=zscore(data)

    # 結果を表示する
    print(data)
    print(normalization_data)

if __name__ == '__main__':
    z_score_normalize_data(data)
