import os
import cv2
import utils

image = cv2.imread("./static/images/0d7d365d6bf81df5372e2d7142b9cc88.png")
chars = utils.extract_chars(image)

for char in chars:
    cv2.imshow('Image', char[1])
    input = cv2.waitKey(0)
    resized = cv2.resize(char[1], (20, 20))
    if 48 <= input <= 57:
        name = str(input - 48)
        file_count = len(next(os.walk('./training_data/' + name + '/'))[2])
        cv2.imwrite('./training_data/' + str(input - 48) + '/' + str(file_count + 1) + '.png', resized)
    elif input == ord('+') or input == ord('-') or input == ord('x'):
        print(input)
        if input == ord('+'):
            name = '10'
        if input == ord('-'):
            name = '11'
        if input == ord('x'):
            name = '12'
        #
        # name = str(input - ord('a') + 10)
        file_count = len(next(os.walk('./training_data/' + name + '/'))[2])
        cv2.imwrite('./training_data/' + name + '/' + str(file_count + 1) + '.png', resized)
