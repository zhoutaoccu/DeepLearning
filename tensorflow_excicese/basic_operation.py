# -*- encoding: utf-8 -*-
"""
    Topic: Tensorflow
    Desc : 基本运算
"""
__author__ = 'Zhoutaoccu'
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' ##避免出现警告，说CPU编译可以换更好地编译方式

import tensorflow as tf
## Define constant
a=tf.constant(1)
b=tf.constant(2)

with tf.Session() as sess:
    print("a: %i" %sess.run(a), "b: %i" %sess.run(b))
    print(sess.run(a+b))
    print(sess.run(a*b))
## Define variable as graph input
a=tf.placeholder(tf.int16)
b=tf.placeholder(tf.int16)
## Define function
add=tf.add(a,b)
mul=tf.multiply(a,b)
## Launch the graph
with tf.Session() as sess:
    print(sess.run(add,feed_dict={a:5,b:6}))
    print(sess.run(mul, feed_dict={a: 5, b: 6}))

## For matrix
matrix1=tf.constant([[1,3]])
matrix2=tf.constant([[2],[4]])
product=tf.matmul(matrix1,matrix2)
with tf.Session() as sess:
    print(sess.run(product))

hello=tf.constant('Hello TensorFlow!')
sess=tf.Session() #tensorflow主要的运算操作
print(sess.run(hello).decode()) #b:表示字节编码(bytes)字符串，加上decode()去掉

##计算图（Graph）:搭建神经网络的计算过程，只搭建，不运算
import tensorflow as tf
x=tf.constant([[1.0,2.0]])
w=tf.constant([[3.0],[4.0]])
y=tf.matmul(x,w)
print(y)

##会话（Session）:执行计算图中的节点运算
with tf.Session() as sess:
    print(sess.run(y))
