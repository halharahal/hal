#coding:utf-8
import scipy.stats as spstat
import numpy as np

# データ
list = np.array([10, 20, 20, 20, 20, 20, 100, 1000, 4000])

def mode():

    # 中央値の計算
    mode = spstat.mode(list)

    # 結果の表示
    print(u"最頻値："+str(mode))

if __name__ == '__main__':
    mode()