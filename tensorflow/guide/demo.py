#!/usr/bin/env python3
import tensorflow as tf


w = tf.get_variable('weights', initializer=tf.constant([[1, 2, 3]]))
b = tf.get_variable('bias', initializer=tf.constant([4]))

x = tf.placeholder(dtype=tf.int32, shape=[3, 1])
print(w, x, b)
y = tf.matmul(w, x) + b

sess = tf.Session()
sess.run(tf.global_variables_initializer())

print(sess.run(y, feed_dict={x: [[1], [2], [3]]}))
