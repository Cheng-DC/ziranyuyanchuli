import nltk
nltk.data.path.append("G:\\自然语言\\nltk_data-gh-pages\\packages")
# 1.古腾堡语料库
print("获取古腾堡语料库:", "\n", nltk.corpus.gutenberg.fileids()) # 获取古腾堡语料库
emma = nltk.corpus.gutenberg.words("austen-emma.txt")
print(emma)
emma_sent = nltk.corpus.gutenberg.sents("austen-emma.txt")
print(emma_sent)# 文件要重新添加索引
from nltk.corpus import gutenberg # 加载古腾堡语料库
for fileid in gutenberg.fileids():
    raw = gutenberg.raw(fileid) # 给出原始内容
    # print(raw)
    words = gutenberg.words(fileid) #获取文本的词
    sents = gutenberg.sents(fileid) #获取文本的句子
    print(fileid, len(raw), len(words), len(sents))
# 3.聊天会话语料库
from nltk.corpus import nps_chat
print(nps_chat.fileids())
words = nps_chat.words("10-19-20s_706posts.xml")
print(words)
chatroom = nps_chat.words("10-19-20s_706posts.xml")
print(chatroom)
# 4.布朗语料库
from nltk.corpus import brown
print(brown.categories())
print(brown.words(categories="news"))
tag = brown.tagged_words(categories="news", tagset="universal")
print(tag)
fdist = nltk.FreqDist([tag for (word, tag) in tag])
print(fdist.most_common(10))
