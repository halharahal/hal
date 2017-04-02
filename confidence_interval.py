# coding:utf-8

import numpy as np
from scipy import stats

# サンプル数
sample_number = 10000

# 有意水準：帰無仮説を棄却するために、あらかじめ決めた確率水準のこと。ここでは信頼係数95%とする
alpha = 0.95

def confidence_interval(sample_number,alpha):

    # 標準正規分布に従うデータをsample_number個分だけ生成する
    sample_data = np.random.randn(sample_number)

    # 生成したデータの平均値を求める
    mean_value = np.mean(sample_data)

    # 平均値の標準誤差(SEM)を求める
    sem_value = stats.sem(sample_data)

    # 期待値loc，標準偏差scaleの正規分布のalphaぶんだけの分布が含まれる範囲を，メディアンを中心に取得する
    min,max = stats.t.interval(alpha, len(sample_data) - 1, loc=mean_value, scale=sem_value)

    print(u'信頼区間の下限値:'+ str(min))
    print(u'信頼区間の上限値:'+ str(max))


if __name__ == '__main__':
    confidence_interval(sample_number,alpha)