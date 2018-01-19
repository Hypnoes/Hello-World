import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2, 3]))
w2 = tf.Variable(tf.random_normal([3, 1]))

x = tf.placeholder(tf.float32, shape=(3, 2), name="INPUT")
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

fd = {
    x: [[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]
}
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    print(sess.run(y, feed_dict=fd))

# 定义损失函数来刻画与预测值与真实值的差距
cross_entropy = -tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
)

# 定义学习率
learning_rate = 0.001

# 定义反向传播算法来优化神经网络的参数
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)
