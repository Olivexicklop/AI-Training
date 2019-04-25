import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization

def Alexnet(width, height, lr):
	net = input_data(shape=[None, width, height, 1], name='input')
	net = conv_2d(net, 96, 11, strides=4, activation='relu')
	net = max_pool_2d(net, 3, strides=2)
	net = local_response_normalization(net)
	net = conv_2d(net, 256, 5, activation='relu')
	net = max_pool_2d(net, 3, strides=2)
	net = local_response_normalization(net)
	net = conv_2d(net, 384, 3, activation='relu')
	net = conv_2d(net, 384, 3, activation='relu')
	net = conv_2d(net, 256, 3, activation='relu')
	net = max_pool_2d(net, 3, strides=2)
	net = local_response_normalization(net)
	net = fully_connected(net, 4096, activation='tanh')
	net = dropout(net, 0.5)
	net = fully_connected(net, 4096, activation='tanh')
	net = dropout(net, 0.5)
	net = fully_connected(net, 17, activation='softmax')
	net = regression(net, optimizer='momentum', loss='categorical_crossentropy', learning_rate=0.001)






