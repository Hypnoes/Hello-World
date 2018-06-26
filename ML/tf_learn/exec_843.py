#!python3
# -*- coding: utf-8 -*-

import logging
logging.getLogger().setLevel(logging.ERROR)

import numpy as np
import tensorflow as tf

# 加载matplotlib工具包，绘制结果图像
import matplotlib as mpl
mpl.use('Agg')

from matplotlib import pyplot as plt

learn = tf.contrib.learn

HIDDEN_SIZE = 30              # LSTM中隐藏节点的个数
NUM_LAYERS = 2                # LSTM的层数

TIMESTEPS = 10                # RNN的截断长度
TRAINING_STEPS = 10000        # 训练轮数
BATCH_SIZE = 32               # batch大小

TRAINING_EXAMPLES = 10000     # 训练数据的个数
TESTING_EXAMPLES = 1000       # 测试数据的个数
SAMPLE_GAP = 0.01             # 采样间隔

def generate_data(seq):
    X = []
    y = []
    # 序列的第i项和后面的TIMESTEPS - 1项合在一起错位输入，第i + TIMESTEPS项
    # 作为输出。即用sin函数前的TIMESTEPS个点的信息，预测第i + TIMESTEPS个点
    # 的函数值
    for i in range(len(seq) - TIMESTEPS - 1):
        X.append([seq[i: i + TIMESTEPS]])
        y.append([seq[i + TIMESTEPS]])
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)

def lstm_model(X, y):
    # 使用多层LSTM结构
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(HIDDEN_SIZE)
    cell = tf.nn.rnn_cell.MultiRNNCell([lstm_cell] * NUM_LAYERS)
    x_ = tf.unstack(X, axis=1)

    # 使用tensorflow接口将多层的LSTM解构连接成RNN并计算向前传播的结果
    output, _ = tf.nn.static_rnn(cell, x_, dtype=tf.float32)
    # 在本问题钟只关注最后一个时刻的输出，该结果作为下一时刻的预测值
    output = output[-1]

    # 对LSTM网络的输出再加一层全连接层并计算损失，默认损失为
    # 平均平方差损失函数
    prediction, loss = learn.models.linear_regression(output, y)

    # 创建模型优化器并得到优化步骤
    train_op = tf.contrib.layers.optimize_loss(
        loss,
        tf.contrib.framework.get_global_step(),
        optimizer='Adagrad',
        learning_rate=0.1
    )

    return prediction, loss, train_op

# 建立深层循环神经网络
regressor = learn.Estimator(model_fn=lstm_model)

# 用正弦函数生成训练和测试数据集
test_start = TRAINING_EXAMPLES * SAMPLE_GAP
test_end = (TRAINING_EXAMPLES + TESTING_EXAMPLES) * SAMPLE_GAP
train_X, train_y = generate_data(np.sin(np.linspace(
    0, test_start, TRAINING_EXAMPLES, dtype=np.float32
)))
test_X, test_y = generate_data(np.sin(np.linspace(
    test_start, test_end, TESTING_EXAMPLES, dtype=np.float32
)))

# 使用fit函数训练模型
regressor.fit(train_X, train_y, batch_size=BATCH_SIZE, steps=TRAINING_STEPS)

# 对训练的模型进行测试
predicted = [[pred] for pred in regressor.predict(test_X)]
rmse = np.sqrt(((predicted - test_y) ** 2).mean(axis=0))
print(f'Mean Square Error is : {rmse[0]}')

# 绘制预测的结果图像
fig = plt.figure()
plot_predicted = plt.plot(predicted, label='predicted')
plot_test = plt.plot(test_y, label='real_sin')
plt.legend([plot_predicted, plot_test], ['predicted', 'real_sin'])

fig.savefig('sin.png')
