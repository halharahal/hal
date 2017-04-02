# coding:utf-8

data = [
    (1, 1), (2, 1), (3, 2), (4, 3),
    (5, 5), (6, 7), (7, 6), (8, 8),
    (9, 9), (10, 11), (11, 10), (12, 13),
    (13, 15), (14, 12), (15, 23), (16, 14),
    (17, 19), (18, 16), (19, 20), (20, 15),
]

def correlation_coefficient_spearman(data):
    d = 0
    n = len(data)

    for x, y in data:
        d += (x - y)*(x - y)

    print(u"スピアマンの相関係数:"),
    print(1.0 - 6.0 * d / (n ** 3 - n))

if __name__ == '__main__':
    correlation_coefficient_spearman(data)
