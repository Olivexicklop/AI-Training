import numpy as np
from PIL import ImageGrab
import cv2
import time
from SimulateKeypress import PressKey, ReleaseKey, W, A, S, D
from GrabScreen import grab_screen
from GetKeys import key_check
# import pyautogui
import os



def KeysOutput(keys):
	#[A,W,D]
	output = [0,0,0]

	if 'A' in keys:
		output[0] = 1
	elif 'W' in keys:
		output[1] = 1
	elif 'D' in keys:
		output[2] = 1

	return output




def RegionOfInterest(img, vertices):
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, vertices, 255)
	masked = cv2.bitwise_and(img, mask)
	return masked






file_name = 'training_data.npy'

if os.path.isfile(file_name):
	print('Success')
	training_data = list(np.load(file_name))
else:
	print('Failed')
	training_data = []


for i in range(3,0,-1):
	print(i)
	time.sleep(1)
	i -= 1

last_time = 0

while (True):
	# screen_img = np.array(ImageGrab.grab(bbox=(0,40,800,600)))
	screen_img = grab_screen(region=(0,40,800,600))
	screen_img = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)
	screen_img = cv2.resize(screen_img, (80,60))
	# processed_screen_img = ProcessImg(screen_img)
	keys = key_check()
	output = KeysOutput(keys)
	training_data.append([screen_img,output])

	#print('took {} seconds'.format(time.time() - last_time))
	last_time = time.time()
	# screen_numpy = np.array(screen_img.getdata(),dtype='uint8').reshape((screen_img.size[1],screen_img.size[0],3))
	#ImgToShow = cv2.cvtColor(processed_screen_img, cv2.COLOR_BGR2RGB)


	if len(training_data) % 500 == 0:
		print(len(training_data))
		np.save(file_name, training_data)
















