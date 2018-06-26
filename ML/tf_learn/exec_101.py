import tensorflow as tf

g1 = tf.Graph()
with g1.as_default():
    # Define variable "v" in calculate graph g1, and initialized with 0
    v = tf.get_variable(
        "v", initializer = tf.zeros_initializer(), shape=[1]
    )

g2 = tf.Graph()
with g2.as_default():
    # Define variable "v" in calculate graph g2, and initialized with 1
    v = tf.get_variable(
        "v", initializer = tf.ones_initializer(), shape=[1]
    )

# Read variable "v" in g1
with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        # Output [0.], var "v" is 0 in graph g1
        print(sess.run(tf.get_variable("v")))

# Read variable "v" in g2
with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope("", reuse=True):
        # Output [1.], var "v" is 1 in graph g2
        print(sess.run(tf.get_variable("v")))

