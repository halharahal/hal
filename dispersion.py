#coding:utf-8
import numpy as np

# データ
list = np.array([3, 4, 5, 5, 7, 8])

def dispersion():

    # 分散の計算
    dispersion = np.var(list)

    # 結果の表示
    print(u"分散："+str(dispersion))

if __name__ == '__main__':
    dispersion()