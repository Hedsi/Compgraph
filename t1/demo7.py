import numpy as np
import cv2

from circle import circle

width = 740
height = 580

img = np.full((height, width, 3), 255, dtype=np.uint8)

cx = width // 2
cy = height // 2

for r in range(5, 101, 5):
    circle(img, cx, cy, r, (0, 0, 0))

cv2.imwrite("out/task07.png", img)
print("Зображення збережено: out/task07.png")