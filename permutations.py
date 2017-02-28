#coding:utf-8
import itertools

# 並べる対象
n = ['J', 'Q', 'K']

# 並べる数
m = 2


def permutations(n,m):

    # list化
    l = list(itertools.permutations(n,m));

    # パターン表示
    print l

    # パターン数取得
    pattern = len(l)

    #パターン数表示
    print pattern

if __name__ == '__main__':
    permutations(n,m);