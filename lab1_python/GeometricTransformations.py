import cv2
import numpy as np
import math

image = cv2.imread('forest.jpg')
cv2.imshow('original', image)

# rotation and translation variables and matrices
t1 = 0
t2 = 0
a = math.pi/2
#a = 0
translation_matrix = np.array([[1, 0, t1],
                               [0, 1, t2],
                               [0, 0, 1]])
rotation_matrix = np.array([[math.cos(a), -math.sin(a), 0],
                            [math.sin(a), math.cos(a), 0],
                            [0, 0, 1]])
translate_rotate_matrix = np.array([[math.cos(a), -math.sin(a), t1],
                                    [math.sin(a), math.cos(a), t2],
                                    [0, 0, 1]])

# Performs rotation then translation (Uses nearest neighbor)
new_image = np.full_like(image, 255)
for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        values = np.array([x, y, 1])
        values = np.matmul(rotation_matrix, values)
        values = np.matmul(translation_matrix, values)
        if new_image.shape[0] > values[0] > 0 and new_image.shape[1] > values[1] > 0:
            new_image[int(values[0])][int(values[1])] = image[x][y]

# Performs rotation and translation simultaneously (Uses nearest neighbor)
new_image2 = np.full_like(image, 255)
for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        values = np.array([x, y, 1])
        values = np.matmul(translate_rotate_matrix, values)
        if new_image2.shape[0] > values[0] > 0 and new_image2.shape[1] > values[1] > 0:
            new_image2[int(values[0])][int(values[1])] = image[x][y]

cv2.imshow('original', image)
cv2.imshow('translated Image', new_image)
cv2.imshow('translated rotated Image 2', new_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()