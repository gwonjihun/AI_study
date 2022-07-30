import cv2
import utils

BLUE = 0
GREEN = 1 
RED = 2

image = cv2.imread("./static/images/1e533ad5cecdfef95711eb43f4dbc1f5.png", cv2.IMREAD_COLOR)
blue = utils.get_chars(image.copy(), utils.BLUE)
red = utils.get_chars(image.copy(), utils.RED)
green = utils.get_chars(image.copy(), utils.GREEN)
cv2.imshow('Image Gray', blue)
cv2.waitKey(0)
cv2.imshow('Image Gray', red)
cv2.waitKey(0)
cv2.imshow('Image Gray', green)
cv2.waitKey(0)
