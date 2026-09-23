import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split


def generate_data(seq_length=100, n_samples=10000):
    """生成正弦和余弦序列对"""
    X = []
    y = []
    for _ in range(n_samples):
        # 随机生成相位偏移和频率
        offset = np.random.random() * 2 * np.pi
        freq = np.random.random() * 0.1 + 0.05

        # 生成时间序列
        t = np.linspace(0, 100, seq_length)

        # 生成sin和cos序列
        sin_seq = np.sin(freq * t + offset)
        cos_seq = np.cos(freq * t + offset)

        # 随机决定是sin转cos还是cos转sin
        if np.random.random() > 0.5:
            X.append(sin_seq)
            y.append(cos_seq)
        else:
            X.append(cos_seq)
            y.append(sin_seq)

    return np.array(X), np.array(y)


def build_lstm_model(input_shape):
    """构建LSTM模型"""
    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=input_shape),
        LSTM(32, return_sequences=True),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    return model


def plot_results(model, X_test, y_test, num_samples=3):
    """可视化预测结果"""
    plt.figure(figsize=(15, 5 * num_samples))

    for i in range(num_samples):
        idx = np.random.randint(0, len(X_test))
        test_sample = X_test[idx]
        true_output = y_test[idx]

        # 进行预测
        predicted = model.predict(test_sample[np.newaxis, ...])

        # 绘制结果
        plt.subplot(num_samples, 1, i + 1)
        plt.plot(test_sample, label='Input')
        plt.plot(true_output, label='True Output')
        plt.plot(predicted[0], '--', label='Predicted')
        plt.legend()
        plt.title(f'Sample {i + 1}')

    plt.tight_layout()
    plt.show()


def main():
    # 1. 生成数据
    print("Generating data...")
    X, y = generate_data(seq_length=100, n_samples=10000)

    # 2. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 调整数据形状以适应LSTM输入 (样本数, 时间步长, 特征数)
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    y_train = y_train.reshape((y_train.shape[0], y_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
    y_test = y_test.reshape((y_test.shape[0], y_test.shape[1], 1))

    # 4. 构建模型
    print("Building model...")
    model = build_lstm_model((X_train.shape[1], X_train.shape[2]))
    model.summary()

    # 5. 训练模型
    print("Training model...")
    history = model.fit(
        X_train, y_train,
        epochs=50,
        batch_size=32,
        validation_data=(X_test, y_test),
        verbose=1
    )

    # 6. 绘制训练过程
    plt.figure(figsize=(10, 5))
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('MSE Loss')
    plt.legend()
    plt.title('Training and Validation Loss')
    plt.show()

    # 7. 可视化预测结果
    print("Plotting results...")
    plot_results(model, X_test, y_test, num_samples=3)


if __name__ == "__main__":
    main()