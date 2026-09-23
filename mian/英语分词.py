import nltk
import re
nltk.data.path.append("G:\\自然语言\\nltk_data-gh-pages\\packages")
text = "The pendant of the necklace was a one-yuan coin with a hole drilled in it. When Bai Liu put his hand on it, sure enough, the game interface popped up. The interface was the same as before, without any additional information."
text = re.sub(r"[\,\!\.]", "", text)
print(text)
text_words = nltk.tokenize.word_tokenize(text)
print(text_words)
text_words = text.split(" ")
print(text_words)
