#coding:utf-8
import numpy as np

# データ
list = np.array([10, 20, 50, 100, 100000])

def median():

    # 中央値の計算
    median = np.median(list)

    # 結果の表示
    print(u"中央値："+str(median))

if __name__ == '__main__':
    median()