import numpy as np
from PIL import ImageGrab
import cv2
import time
from SimulateKeypress import PressKey, ReleaseKey, W, A, S, D
# import pyautogui

def RegionOfInterest(img, vertices):
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, vertices, 255)
	masked = cv2.bitwise_and(img, mask)
	return masked


def DrawLines(img, roadLine):
	try:
		for line in roadLine:
			
	except:

def ProcessImg(OriginalImg):
	ProcessedImg = cv2.cvtColor(OriginalImg, cv2.COLOR_BGR2GRAY)

	ProcessedImg = cv2.Canny(ProcessedImg, threshold1=200, threshold2=300)
	
	ProcessedImg = cv2.GaussianBlur(ProcessedImg, (5,5), 0) 

	vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500]])
	ProcessedImg = RegionOfInterest(ProcessedImg,[vertices])
	
	roadLine = cv2.HoughLinesP(ProcessedImg, 1, np.pi/180, 180, 20, 15)
	DrawLines(OriginalImg, roadLine)


	return ProcessedImg


for i in range(3,0,-1):
	print(i)
	time.sleep(1)
	i -= 1



while (True):
	screen_img = np.array(ImageGrab.grab(bbox=(0,40,800,600)))
	processed_screen_img = ProcessImg(screen_img)
	# screen_numpy = np.array(screen_img.getdata(),dtype='uint8').reshape((screen_img.size[1],screen_img.size[0],3))
	#ImgToShow = cv2.cvtColor(processed_screen_img, cv2.COLOR_BGR2RGB)
	
	# print("down")
	# PressKey(W)
	# time.sleep(3)
	# ReleaseKey(W)
	# print("up")

	# cv2.resizeWindow("window",800,600)
	cv2.imshow('window',processed_screen_img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break