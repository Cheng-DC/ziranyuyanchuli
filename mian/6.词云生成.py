from wordcloud import WordCloud
import jieba
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import platform


def read_stop_words(file_path):
    stop_words = []
    with open(file_path, encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            stop_words.append(line)
    stop_words = list(set(stop_words))
    return stop_words


def cut_text(text_path):
    with open(text_path, encoding="utf-8") as f:
        text = f.read()
    result_text = jieba.lcut(text)
    result_text = " ".join(result_text)
    return result_text


def use_mask(mask_path):
    mask = Image.open(mask_path)
    mask = np.array(mask)
    return mask


def word_cloud(text, stop_words, mask):
    # 根据操作系统选择合适的字体路径
    if platform.system() == "Windows":
        font_path = "C:/Windows/Fonts/msyh.ttc"  # Windows系统字体路径
    elif platform.system() == "Darwin":  # macOS
        font_path = "/System/Library/Fonts/PingFang.ttc"
    else:  # Linux
        font_path = "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf"

    try:
        # 创建词云对象
        wordCloud = WordCloud(
            font_path=font_path,
            width=1700,
            height=1700,
            background_color='white',
            stopwords=stop_words,
            max_words=50,
            mask=mask,
            contour_width=1,
            contour_color='steelblue'
        )

        # 生成并显示词云
        wordCloud.generate(text)
        plt.figure(figsize=(12, 10))
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis("off")

        # 保存词云图片
        output_path = "result/wordcloud_output.png"
        wordCloud.to_file(output_path)
        print(f"词云已成功保存至: {output_path}")

        plt.show()
    except Exception as e:
        print(f"生成词云时出错: {e}")
        # 尝试使用默认字体作为备选方案
        print("尝试使用默认字体...")
        wordCloud = WordCloud(
            width=1700,
            height=1700,
            background_color='white',
            stopwords=stop_words,
            max_words=50,
            mask=mask
        )
        wordCloud.generate(text)
        wordCloud.to_file("data/wordcloud_fallback.png")
        print("已使用默认字体生成备选词云: data/wordcloud_fallback.png")


if __name__ == '__main__':
    # 1.获取停用词
    stop_file_path = "data/2.text"
    stop_words = read_stop_words(stop_file_path)
    print(f"加载停用词: {len(stop_words)}个")

    # 2.获取文本，进行分词
    text_path = "data/精封.text"
    text = cut_text(text_path)
    print("文本分词完成")

    # 3.获取剪影
    mask_path = "data/alice_mask.png"
    try:
        mask = use_mask(mask_path)
        print("掩码图片加载成功")
    except Exception as e:
        print(f"加载掩码图片失败: {e}")
        mask = None

    # 4.生成词云
    word_cloud(text, stop_words, mask)