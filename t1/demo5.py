import math
import numpy as np
import cv2

from line import line

width = 740
height = 580

img = np.full((height, width, 3), 255, dtype=np.uint8)

cx = width // 2
cy = height // 2
radius = 270

ray_count = 29

for i in range(ray_count):
    angle = 2 * math.pi * i / ray_count

    x1 = cx + round(radius * math.cos(angle))
    y1 = cy + round(radius * math.sin(angle))

    line(img, cx, cy, x1, y1, (0, 0, 0))

cv2.imwrite("out/task05.png", img)
print("Зображення збережено: out/task05.png")