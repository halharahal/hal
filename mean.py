#coding:utf-8
import numpy as np

# データ
list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def mean():

    # 平均値の計算
    mean = np.mean(list)

    # 結果の表示
    print(u"平均値："+str(mean))

if __name__ == '__main__':
    mean()