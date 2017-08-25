import re
import MeCab

mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")
text = "おじいさんは山へ芝刈りに、おばあさんは川へ洗濯に行きました。"
words = []

node = mecab.parseToNode(text)
while node:
    if node.feature.split(',')[0] == '名詞':
        word = node.feature.split(",")[6]
        words.append(word)
    node = node.next
print(" ".join(words))
