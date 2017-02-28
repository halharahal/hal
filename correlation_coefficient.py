# coding:utf-8
import numpy as np

# 来客数
x = [220,250,270,300,350,400,410,450,510,580]
# 売上高
y = [120,150,140,210,201,280,204,290,310,370]

def correlation_coefficient(x,y):

    # 相関係数の計算
    corr = np.corrcoef(x, y)

    # 結果の表示
    print(u"相関係数：" + str(corr[0,1]))


if __name__ == '__main__':
    correlation_coefficient(x,y)
