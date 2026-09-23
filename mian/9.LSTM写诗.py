import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import string

# 简单的诗歌数据集
poetry_corpus = """
    "床前明月光，疑是地上霜。举头望明月，低头思故乡。",
    "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
    "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。",
    "红豆生南国，春来发几枝。愿君多采撷，此物最相思。
"""


# 数据预处理
def preprocess_text(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    return text


processed_corpus = preprocess_text(poetry_corpus)

# 创建字符到索引和索引到字符的映射
chars = sorted(list(set(processed_corpus)))
char_to_idx = {c: i for i, c in enumerate(chars)}
idx_to_char = {i: c for i, c in enumerate(chars)}

# 准备训练数据
seq_length = 10
step = 1
sentences = []
next_chars = []

for i in range(0, len(processed_corpus) - seq_length, step):
    sentences.append(processed_corpus[i: i + seq_length])
    next_chars.append(processed_corpus[i + seq_length])

# 向量化
x = np.zeros((len(sentences), seq_length, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_to_idx[char]] = 1
    y[i, char_to_idx[next_chars[i]]] = 1

# 构建LSTM模型
model = Sequential([
    LSTM(128, input_shape=(seq_length, len(chars))),
    Dense(len(chars), activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam')

# 训练模型
model.fit(x, y, batch_size=64, epochs=100, verbose=2)


# 采样函数
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


# 生成诗歌
def generate_poem(seed_text, length=100, temperature=0.5):
    generated = seed_text
    sentence = seed_text

    for i in range(length):
        x_pred = np.zeros((1, seq_length, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_to_idx[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, temperature)
        next_char = idx_to_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

    return generated


# 设置随机种子以获得可重复的结果
np.random.seed(42)
tf.random.set_seed(42)

# 生成一首诗
seed = "红"
poem = generate_poem(seed, length=40, temperature=0.7)

print("LSTM创作的诗：")
print("=" * 20)
print(poem)
print("=" * 20)