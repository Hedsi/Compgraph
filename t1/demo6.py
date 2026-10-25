import numpy as np
import cv2

from line import line, thick_line

height, width = 160, 360
img = np.full((height, width, 3), 255, dtype=np.uint8)


A1 = (20, 30)
B1 = (31, 33)
line(img, *A1, *B1, (255, 0, 0))

A2 = (200, 30)
B2 = (211, 33)
cv2.line(img, A2, B2, (0, 0, 255), 1)


thick_line(img, (20, 80), (140, 110), (0, 180, 0), 7)
cv2.line(img, (200, 80), (320, 110), (0, 180, 0), 7)

cv2.imwrite("out/task06.png", img)


a = np.zeros((20, 20, 3), dtype=np.uint8)
b = np.zeros_like(a)

line(a, 2, 2, 13, 5, (255, 255, 255))
cv2.line(b, (2, 2), (13, 5), (255, 255, 255), 1)

different = np.any(a != b, axis=2)
print("Кількість пікселів, що відрізняються:", np.count_nonzero(different))
print("Зображення збережено: out/task06.png")