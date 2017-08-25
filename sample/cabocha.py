import CaboCha

c = CaboCha.Parser()

text = "太郎は花子が読んでいる本を次郎に渡した"

tree = c.parse(text)
chunks = {}
for i in range(tree.chunk_size()):
    chunk = tree.chunk(i)
    token = ''
    for j in range(chunk.token_size):
        token += tree.token(chunk.token_pos + j).surface
    chunks[i] = token

for i in range(tree.chunk_size()):
    chunk = tree.chunk(i)
    if chunk.link != -1:
        target = chunks[chunk.link]
    else:
        target = 'EOS'
    print(chunks[i], '->', target)
