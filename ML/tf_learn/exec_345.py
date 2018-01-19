import tensorflow as tf

# numpy是一个科学计算的工具包,这里通过NumPy工具包生成模拟数据
from numpy.random import RandomState

# 定义训练数据batch的大小
batch_size = 8

# 定义神经网络的参数
w1 = tf.Variable(tf.random_normal([2, 3], seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], seed=1))

# 在shape的一个维度上使用None可以方便的使用不大的batch大小. 在训练需要吧数据分为
# 较小的batch时, 但是在测试时, 可以一次使用全部的数据. 当数据集比较小时这样比较
# 方便测试, 但是数据集比较大时, 将大量数据放入一个batch可能会内存溢出
x = tf.placeholder(tf.float32, shape=(None, 2), name="x-input")
y_ = tf.placeholder(tf.float32, shape=(None, 1), name="y-input")

# 定义前向传播的过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播过程
cross_entropy = - tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
)
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 生成一个随机的模拟数据集
# 这里将所以x1 + x2 < 1的样本几位正样本,其余为负. 正样本表示为1, 负样本表示为0
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

# 创建一个会话来运行tensorflow程序
with tf.Session() as sess:
    # 初始化变量
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    # 训练前的权重矩阵
    print("w1:", sess.run(w1))
    print("w2:", sess.run(w2))

    # 设定训练次数
    STEPS = 5000
    for i in range(STEPS):
        # 每次选取batch_size个样本进行训练
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)

        # 用过选取的样本训练神经网络并更新参数
        sess.run(train_step, 
            feed_dict={ x: X[start:end], y_: Y[start:end] }
        )

        if i % 1000 == 0:
            # 每隔一段时间计算所有数据上的交叉熵并输出
            total_cross_entropy = sess.run(
                cross_entropy, feed_dict={ x: X, y_: Y }
            )

            print("After %d training step(s), cross entropy on all data is %g" %
                (i, total_cross_entropy)
            )

    # 训练后权重的变化
    print("w1:", sess.run(w1))
    print("w2:", sess.run(w2))
