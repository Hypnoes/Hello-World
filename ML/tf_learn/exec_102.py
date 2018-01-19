import tensorflow as tf

# 声明w1, w2两个变量, seed为随机种子
# seed=1表示每次随机的结果一样
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1.0, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1.0, seed=1))

# 输入的特征向量为一个常量,这里x为1 * 2的矩阵
x = tf.constant([[0.7, 0.9]])

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

with tf.Session() as sess:
    # 注意不能直接Session.run(), 因为w1, w2还没有初始化
    sess.run(w1.initializer)
    sess.run(w2.initializer)

    # 输出为[[3.957578]]
    print(sess.run(y))
