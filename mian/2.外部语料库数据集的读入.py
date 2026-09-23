import nltk
# 聊天会话语料库
nltk.data.path.append("G:\\自然语言\\nltk_data-gh-pages\\packages")
from nltk.corpus import nps_chat
print(nps_chat.fileids())