#coding:utf-8
import numpy as np

# データ
list = np.array([3, 4, 5, 5, 7, 8])

def dispersion():

    # 分散の計算
    std = np.std(list)

    # 結果の表示
    print(u"標準偏差："+str(std))

if __name__ == '__main__':
    dispersion()