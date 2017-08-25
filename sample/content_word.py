import MeCab
m = MeCab.Tagger()

text = "ある日の暮方の事である。一人の下人が、羅生門の下で雨やみを待っていた"
words = []
node = m.parseToNode(text)
while node:
    parts_of_speech = node.feature.split(',')[0]
    if parts_of_speech in ['名詞', '動詞', '形容詞', '副詞', '接続詞', '接頭詞', '連体詞', '感動詞']:
        original = node.feature.split(',')[6]
        if original == '*':
            original = node.surface
        words.append(original)
    node = node.next

print(words)
