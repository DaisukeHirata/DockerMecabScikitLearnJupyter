import MeCab
mecab = MeCab.Tagger()

with open('wikipedia_言語.txt') as f:
    node = mecab.parseToNode(f.read())
    words = {}
    while node:
        if node.feature.split(',')[0] == '名詞':
            if node.surface in words:
                words[node.surface] += 1
            else:
                words[node.surface] = 1
        node = node.next
    for tpl in sorted(words.items(), key=lambda x: x[1], reverse=True)[0:10]:
        print(tpl)
