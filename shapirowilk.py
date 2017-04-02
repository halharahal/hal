# coding:utf-8
import numpy as np
import scipy.stats as stats

normal=np.random.normal(100, 10, 1000)  #平均:100, 分散:10の正規分布に従う乱数を 1000 件出力

def shapirowilk(normal):

    # 検定値とp値の計算
    w,p=stats.shapiro(normal)

    # 検定値の表示
    print(u"検定値: " + str(w))

    # p値の表示
    print(u"p値：" + str(p))

if __name__ == '__main__':
    shapirowilk(normal)
