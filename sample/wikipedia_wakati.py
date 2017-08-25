import glob
import os
import re
import sys
import MeCab

RE_XML = re.compile("<doc id=\"([0-9]+)\" url=\"([^\"]+)\" title=\"([^\"]+)\"")
RE_MECAB = re.compile("(名詞,一般|名詞,固有名詞|名詞,副詞可能|名詞,サ変接続|名詞,形容動詞語幹|動詞,自立|形容詞,自立)")
RE_EN_SYMBOL = re.compile("^[a-zA-Z0-9!-\/:-@\[-`{-~]")
STOP_WORDS = "する れる いる ある られる なる できる こと もの ため よう"

def single_non_kanji(word):
    return len(word) == 1 and word <= '\u33FF'

def stopword(word):
    return word in STOP_WORDS

def startswith_en_symbol(word):
    return RE_EN_SYMBOL.match(word)

def containable(word):
    return not single_non_kanji(word) and not stopword(word) and not startswith_en_symbol(word)

mecab = MeCab.Tagger("-d/usr/local/lib/mecab/dic/mecab-ipadic-neologd --unk-feature 未知語")
infile = sys.argv[1]
outfile = os.path.splitext(infile)[0].replace("_normalized", "_wakatied") + ".txt"

doc_id = None
words = []
i = 0

with open(outfile, 'w') as fout, open(infile) as fin:
    for line in fin:
        # 記事の開始
        if not doc_id and line.startswith('<doc'):
            doc_id = RE_XML.match(line).group(1)
            words = []
        # 記事の終了
        elif doc_id and line.startswith('</doc'):
            # 30単語以上の記事を用いる
            if len(words) > 30:
                fout.write("{0}\t{1}\n".format(doc_id, " ".join(words)))
            i += 1
            if i % 100 == 0:
                print("{0} documents done.".format(i))
                fout.flush()
            doc_id = None
        # 記事の本文
        else:
            line = line.rstrip()
            node = mecab.parseToNode(line)
            while node:
                feature = node.feature
                if RE_MECAB.match(feature):
                    featurelist = feature.split(",")
                    word = featurelist[6] #dict form
                    word = word.replace(' ', '')
                    if containable(word):
                        words.append(word)
                node = node.next
