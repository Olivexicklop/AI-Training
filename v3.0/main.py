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

file_name = 'training_data.npy'

if os.path.isfile(file_name):
	print('Success')
	training_data = list(np.load(file_name))
else:
	print('Failed')
	training_data = []


# def RegionOfInterest(img, vertices):
# 	mask = np.zeros_like(img)
# 	cv2.fillPoly(mask, vertices, 255)
# 	masked = cv2.bitwise_and(img, mask)
# 	return masked


# def DrawLines(img, roadLine):
# 	try:
# 		for line in roadLine:
			
# 	except:

# def ProcessImg(OriginalImg):
# 	ProcessedImg = cv2.cvtColor(OriginalImg, cv2.COLOR_BGR2GRAY)

# 	ProcessedImg = cv2.Canny(ProcessedImg, threshold1=200, threshold2=300)
	
# 	ProcessedImg = cv2.GaussianBlur(ProcessedImg, (5,5), 0) 

# 	vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500]])
# 	ProcessedImg = RegionOfInterest(ProcessedImg,[vertices])
	
# 	roadLine = cv2.HoughLinesP(ProcessedImg, 1, np.pi/180, 180, np.array([]), 100, 5)
# 	DrawLines(OriginalImg, roadLine)


# 	return ProcessedImg


for i in range(3,0,-1):
	print(i)
	time.sleep(1)
	i -= 1



while (True):
	# screen_img = np.array(ImageGrab.grab(bbox=(0,40,800,600)))
	screen_img = grab_screen(region=(0,40,800,600))
	screen_img = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)
	screen_img = cv2.resize(screen_img, (80,60))
	processed_screen_img = ProcessImg(screen_img)
	keys = key_check()
	output = KeysOutput(keys)
	training_data.append([screen_img,output])
	# screen_numpy = np.array(screen_img.getdata(),dtype='uint8').reshape((screen_img.size[1],screen_img.size[0],3))
	#ImgToShow = cv2.cvtColor(processed_screen_img, cv2.COLOR_BGR2RGB)



	# print("down")
	# PressKey(W)
	# time.sleep(3)
	# ReleaseKey(W)
	# print("up")

	# cv2.resizeWindow("window",800,600)
	# cv2.imshow('window',processed_screen_img)
	# if cv2.waitKey(25) & 0xFF == ord('q'):
	# 	cv2.destroyAllWindows()
	# 	break


	if len(training_data) % 500 == 0:
		print(len(training_data))
		np.save(file_name, training_data)
















