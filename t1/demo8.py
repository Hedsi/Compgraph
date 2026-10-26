import math
import numpy as np
import cv2

from fill import fill_polygon, fill_circle

width = 740
height = 580

img = np.full((height, width, 3), 255, dtype=np.uint8)

left, top = 170, 140
right, bottom = 570, 440
radius = 65
points = []

corners = [
    (right - radius, top + radius, -90),
    (right - radius, bottom - radius, 0),
    (left + radius, bottom - radius, 90),
    (left + radius, top + radius, 180),
]

for cx, cy, start_angle in corners:
    for step in range(19):
        angle = math.radians(start_angle + step * 5)
        x = round(cx + radius * math.cos(angle))
        y = round(cy + radius * math.sin(angle))
        points.append((x, y))

fill_polygon(img, points, (220, 130, 50))

fill_circle(img, 370, 290, 35, (50, 160, 70))

cv2.imwrite("out/task8.png", img)
print("Зображення збережено: out/task08.png")