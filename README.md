# Hello-World
一些随手写的东西 

> 摘自互联网
```python
    # 定义一个LSTM结构。在TensorFlow中通过一句简单的命令就可以实现一个完整的LSTM结构。
    # LSTM钟使用的变量也会在该函数中自动被声明
    lstm = rnn_cell.BasicLSTMCell(lstm_hidden_size)

    # 将LSTM中的状态初始化为全0的数组。和其他神经网络相似，在优化循环神经网络时，每次
    # 也会使用一个batch的训练样本。在以下代码中，batch_size给出了一个batch的大小。
    # BasicLSTMCell类提供了zero_state函数来生成全0的初始状态。
    state = lstm.zero_state(batch_size, tf.float32)

    # 定义损失函数
    loss = 0.0

    # 虽然理论上循环神经网络可以处理任意长度的序列，但是为了避免梯度消散，
    # 会规定一个最大序列长度。num_steps描述了这个长度。
    for i in rante(num_steps):
        # 在第一个时刻声明LSTM结构中使用的变量，在之后的时刻都需要使用之前定义好的变量
        if i > 0:
            tf.get_variable_scope().reuse_variables()

        # 每一步处理时间序列中的一个时刻。当前输入(current_input)和前一时刻的状态
        # (state)传入定义的LSTM结构钟可以得到当前LSTM结构的输出lstm_output和更新后的
        # 状态state。
        lstm_output, state = lstm(current_input, state)
        # 将当前时刻LSTM结构的输出传入一个全连接层得到最后的输出。
        final_output = fully_connected(lstm_output)
        # 计算当前输出的损失
        loss += calc_loss(final_output, expected_output)
```

