# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def create_exp_graph():
    # xの値を生成
    x = np.arange(-5, 5, 0.2)

    # 高さを計算
    exp = np.exp(x) # 指数関数の計算

    # グラフ表示
    plt.plot(x, exp,"-o",lw=2,alpha=0.7,label="exp(x)")

    fn = "Times New Roman"                      # フォント
    plt.tick_params(labelsize=15)               # 軸目盛のフォントサイズ
    plt.xlabel("$x$", fontsize=30, fontname=fn) # x軸のラベル
    plt.ylabel("$y$", fontsize=30, fontname=fn) # y軸のラベル
    plt.title("exp(x)graph", fontsize=25, fontname=fn)  # タイトル
    plt.xlim([-5, 5])                           # x軸の範囲
    plt.ylim([-1, 9])                           # y軸の範囲
    plt.grid()                                  # グリッドの表示
    plt.hlines(y=1, xmin=-5, xmax=5, colors='b', linestyles='dashed', linewidths=1)# y=1の破線
    plt.legend(fontsize=13)                     # 凡例の表示
    plt.show()                                  # グラフの描画

if __name__ == '__main__':
    create_exp_graph()