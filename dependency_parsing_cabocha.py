# -*- coding: utf-8 -*-

import CaboCha

def dependency_parsing(sentence):
    c = CaboCha.Parser()

    tree = c.parse(sentence)

    # 簡易 Tree 表示での出力
    print(tree.toString(CaboCha.FORMAT_TREE) )

    # 計算機に処理しやすいフォーマットで出力
    print(tree.toString(CaboCha.FORMAT_LATTICE))

if __name__ == '__main__':
    # テストデータ作成
    sentence = "halで勉強して優秀なデータサイエンティストになろう。"

    dependency_parsing(sentence)
