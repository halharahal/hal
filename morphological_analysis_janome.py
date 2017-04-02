# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer

def morphological_analysis(data):

    t = Tokenizer()
    tokens = t.tokenize(data)

    print("*********形態素と品詞の出力***********")

    for token in tokens:
        # 品詞を取り出す

        partOfSpeech = token.part_of_speech.split(',')[0]


        print("形態素：",token.surface,"　品詞：",partOfSpeech)

    print("*********各種情報の出力***********")
    for token in t.tokenize(data):
        print(token)

if __name__ == '__main__':
    # テストデータ作成
    data = "halで勉強して優秀なデータサイエンティストになろう。"

    morphological_analysis(data)
