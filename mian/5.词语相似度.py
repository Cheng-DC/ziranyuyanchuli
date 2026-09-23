import jieba
import re
from gensim.models import word2vec


jieba.add_word("打开")
with open('data/精封.text', encoding="utf-8") as f:
    document = f.read()
    document_cut = jieba.cut(document)
    result = ' '.join(document_cut)
    with open('data/2.text', 'w', encoding="utf-8") as f2:
        f2.write(result)
sentences = word2vec.LineSentence("data/2.text")
model = word2vec.Word2Vec(sentences, hs=1, min_count=1, window=5)
print(model.wv["白柳"])
print(model.wv.similarity('精神', '白柳'))
