import numpy as np
from PIL import ImageGrab
import cv2


def ProcessImg(OriginalImg):
	ProcessedImg = cv2.cvtColor(OriginalImg, cv2.COLOR_BGR2GRAY)
	ProcessedImg = cv2.Canny(ProcessedImg, threshold1=200, threshold2=300)
	return ProcessedImg



while (True):
	screen_img = ImageGrab.grab()
	# screen_numpy = np.array(screen_img.getdata(),dtype='uint8').reshape((screen_img.size[1],screen_img.size[0],3))
	ImgToShow = cv2.cvtColor(np.array(screen_img), cv2.COLOR_BGR2RGB)
	cv2.imshow('window',ImgToShow)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break