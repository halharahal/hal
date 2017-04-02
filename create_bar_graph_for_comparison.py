# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

y1 =np.array([  150 ,   20, 10000 ,   10 ,  30])
y2 =np.array([-0.49223434, -0.52511741 , 1.99929095, -0.52764688, -0.45429233])
x  = np.array([1, 2, 3, 4, 5])

def create_bar_graph():
    bar_width = 0.4

    # 標準化前のデータを棒グラフで描画
    plt.ylim([0,15000]) # y軸の範囲: 0<y<10
    plt.bar(x, y1, color = "grey", width = bar_width, label = "row_data", align = "center")
    plt.legend()
    plt.xticks(x + bar_width / 2, ["data1", "data2", "data3", "data4", "data5", ])
    plt.show()

    # 標準化後のデータを棒グラフで描画
    plt.ylim([-1,3]) # y軸の範囲を -1<y<3 に
    plt.hlines(y=[0], xmin=0, xmax=6, linewidths=1)
    plt.bar(x, y2, color = "grey", width = bar_width, label = "normal_data", align = "center")
    plt.legend()
    plt.xticks(x + bar_width / 2, ["data1", "data2", "data3", "data4", "data5", ])
    plt.show()

if __name__ == '__main__':
    create_bar_graph()