import numpy as np
import pandas as pd
from collections import Count
from random import shuffle
import cv2

train_data = np.load('training_data.npy')

df = pd.DataFrame(train_data)

forward = []
left = []
right = []

shuffle(train_data)

for data in train_data:
	img = data[0]
	operation = data[1]

	if operation == [1,0,0]:
		left.append([img,operation])
	elif operation == [0,1,0]:
		forward.append([img,operation])
	elif operation == [0,0,1]:
		right.append([img,operation])

forward = forward[:len(left)]
forward = forward[:len(right)]
left = left[:len(forward)]
right = right[:len(forward)]

final_data = forward + left + right
shuffle(final_data)

np.save('train_data_new.npy')
