import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# MNIST数据集相关常数
INPUT_NODE = 784        # 输入层的节点数. 对于MNIST,表示图片的像素数
OUTPUT_NODE = 10        # 输出层的节点数. 这里表示图片上的数字可能是[0 .. 9]10类

# 深度网络的参数
LAYER1_NODE = 500       # 每个隐藏层有500个节点
BATCH_SIZE = 100        # 每个训练batch中的数据个数.

LEARNING_RATE_BASE = 0.8        # 基础学习率
LEARNING_RATE_DECAY = 0.99      # 学习率衰减
REGULARIZATION_RATE = 0.0001    # 描述模型复杂度的正则化项在损失函数中的系数
TRAINING_STEPS = 30000          # 训练轮数
MOVING_AVERAGE_DACAY = 0.99     # 滑动平均衰减率

# 定义一个辅助函数, 给定神经网络的输入和所有参数, 计算神经网络的前向传播结果.
# 在这里定义了一个使用ReLU激活函数的三层全连接神经网络. 通过加入隐藏层实现了多层
# 网络结构. 这样方便在测试中使用滑动平均模型
def inference(input_tensor, avg_class, weights1, biases1,
    weights2, biases2):
    # 当没有提供滑动平均类时, 直接使用参数当前的取值
    if avg_class == None:
        # 使用ReLU计算隐藏层前向传播结果
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + biases1)
        # 计算输出层的前向传播结果. 因为计算损失函数是会一并计算softmax结果
        # 所以这里不需要计算激活函数. 而且不加入softmax不会影响预测结果. 因为
        # 预测时使用的是不同类别对应节点输出值的相对大小. 有没有softmax层对最后的
        # 分类结果不造成影响. 于是在计算整个神经网络前向传播时可以不计算softmax层
        return tf.matmul(layer1, weights2) + biases2

    else:
        # 首先使用avg_class.average计算得到的变量的滑动平均值
        # 然后计算相应的神经网络的前向传播结果
        layer1 = tf.nn.relu(
            tf.matmul(input_tensor, avg_class.average(weights1)) + 
                avg_class.average(biases1)
        )
        return tf.matmul(layer1, avg_class.average(weights2)) + \
            avg_class.average(biases2)

# 训练模型的过程
def train(mnist):
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')

    # 生成隐藏层的参数
    weights1 = tf.Variable(
        tf.truncated_normal([INPUT_NODE, LAYER1_NODE])
    )
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))

    # 生成输出层的参数
    weights2 = tf.Variable(
        tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE])
    )
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))

    # 计算当前参数下的神经网络前向传播结果. 这里给出的用于计算滑动平均模型为None
    # 所以函数不会使用参数的滑动平均值
    y = inference(x, None, weights1, biases1, weights2, biases2)

    # 定义训练轮数, 此变量不需要计算滑动平均值, 所以这里指定这个变量为
    # 不可训练变量(trainable=False). 在tensorflow训练神经网络时, 一般会将
    # 代表训练轮数的变量标记为不可训练的参数
    global_step = tf.Variable(0, trainable=False)

    # 给定的滑动平均衰减率和训练轮树的变量, 初始化滑动平均类
    # 给定训练轮数的变量可以加快训练早期的变量更新速度
    variable_averages = tf.train.ExponentialMovingAverage(
        MOVING_AVERAGE_DACAY, global_step
    )
    
    # 在所有代表神经网络参数的变量上使用滑动平均. 其他辅助变量(如global_step)就
    # 不需要了. tf.trainable_variables返回上述参数集合GraphKeys.TRAINABLE_VARIABLES
    # 中的元素, 这个集合的元素就是所有没有指定trainable=False的参数
    variable_averages_op = variable_averages.apply(
        tf.trainable_variables()
    )

    # 计算滑动平均值之后的前向传播结果. 滑动平均不会改变变量本身的取值, 而是会维护一个影子
    # 变量来记录其滑动平均值. 所以当需要使用这个滑动平均值时, 需要明确的使用average函数
    average_y = inference(
        x, variable_averages, weights1, biases1, weights2, biases2
    )

    # 计算交叉熵作为刻画预测值和真实值之间的距离的损失函数.这里使用的tensorflow中提供
    # 的sparse_softmax_cross_entropy_with_logits函数来计算交叉熵. 当分类问题只包含
    # 一个正确答案时, 可以使用这个函数来加速交叉熵的计算. MNIST问题图片中只包含0~9中的
    # 一个数字, 所以可以使用这个函数来计算交叉熵的损失. 这个函数的第一个参数是神经网络不
    # 包括softmax层的前向传播结果, 第二个训练参数是正确的答案. 因为标准答案是一个长度为
    # 10的一维数组, 而该函数需要提供的是一个正确答案的数字, 所以需要使用tf.argmax来计算
    # 正确的分类编号
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
        logits=y, labels=tf.argmax(y_, 1)
    )
    # 计算在当前batch钟所有阳历的交叉熵平均值
    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    # 计算L2正则化损失函数
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)

    # 计算模型的正则化损失. 一般只在计算神经网络边上权重的正则化损失, 而不使用偏置项
    regularization = regularizer(weights1) + regularizer(weights2)
    
    # 总损失等于交叉熵损失和正则化损失的和
    loss = cross_entropy_mean + regularization

    # 设置指数衰减的学习率
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,                     # 基础的学习速率
        global_step,                            # 学习率在这个基础上递减
        mnist.train.num_examples / BATCH_SIZE,  # 过完所有训练数据需要的迭代次数
        LEARNING_RATE_DECAY                     # 学习率衰减速度
    )

    # 使用tf.train.GrandientDescentOptimizer优化算法来优化损失函数. 注意这里损失函数
    # 包含了交叉熵损失和L2正则化损失
    train_step = tf.train.GradientDescentOptimizer(learning_rate) \
        .minimize(loss, global_step=global_step)

    # 在训练神经网络模型时, 美国一边数据集需要通过反向传播来更新神经网络中的参数,
    # 又要更新每一个参数的滑动平均值. 为了一次完成多个操作, tensorflow提供了
    # tf.control_dependencies和tf.group两种机制
    with tf.control_dependencies([train_step, variable_averages_op]):
        # 这里和train_op = tf.group(train_step, variables_averages_op)等价
        train_op = tf.no_op(name='train')

    # 检验使用了滑动平均模型的神经网络前向传播结果是否正确. tf.argmax(average_y,1)
    # 计算每一个样例的预测答案. 其中average_y是一个batch_size * 10 的二维数组, 每一行
    # 表示一个样例的前向传播结果. tf.argmax的第二个参数"1"表示选取最大值的操作仅在第一
    # 个维度进行, 也就是, 只在每一行选择最大值对应的下标. 于是得到的结果是一个长度为batch
    # 的一维数组, 这个一维数组中的值就表示了每一个阳历对应的谁表示结果. tf.equal判断
    # 两个张量的每一维否相等, 如果相等则返回True, 否则是False
    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    # 这个运算首先将一个布尔型数值转换为是属性, 然后计算平均值. 这个平均值就是模型在
    # 这一组数据上的正确率
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 初始化会话并开始训练过程
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        # 准备验证数据. 一般在神经网络的训练过程钟会通过验证数据来他只判断停止的
        # 条件和评价训练的效果
        validate_feed = {
            x: mnist.validation.images, 
            y_: mnist.validation.labels
        }
        # 准备测试数据. 在实际项目钟,这部分数据在训练中是不可见的, 这个数据只是作为模型优劣
        # 的评价标准
        test_feed = {
            x: mnist.test.images, y_: mnist.test.labels
        }

        # 迭代训练神经网络
        # 每1000轮输出一次在验证数据集上的测试结果
        for i in range(TRAINING_STEPS):
            if i % 1000 == 0:
                # 计算滑动平均模型在验证数据上的结果. 因为MNIST数据集比较小, 所以一次
                # 可以处理所有的验证数据. 为了计算方便, 本阳历程序没有将验证数据划分为
                # 更小的batch. 当神经网络模型比较复杂或者验证数据比较大时, 太大的batch
                # 会导致计算时内存溢出错误
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print(f"After {i} training step(s), validation accuracy",
                    f"using average model is {validate_acc}")

            # 产生这一轮使用的一个batch的训练数据, 并运行训练过程
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_op, feed_dict={x: xs, y_: ys})

        # 在训练结束后, 在测试数据上检测神经网络的最终正确率
        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print(f"After {TRAINING_STEPS} training step(s), test accuracy using average",
            f"model is {test_acc}")

# 主程序入口
def main(argv=None):
    # 声明处理MNIST数据集的类, 这个类在初始化时会自动下载数据.
    mnist = input_data.read_data_sets("c:\\users\\hypnoes\\desktop\\mnist", one_hot=True)
    train(mnist)

# tensorflow提供了一个主程序入库, tf.app.run会调用上面定义的main函数
if __name__ == '__main__':
    tf.app.run()
