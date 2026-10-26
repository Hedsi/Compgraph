
import os
import math
import numpy as np
import cv2

from fill import fill_polygon, fill_circle
from line import line

os.makedirs("out", exist_ok=True)

WIDTH, HEIGHT = 500, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (220, 120, 40)
RED = (40, 40, 220)

img = np.full((HEIGHT, WIDTH, 3), WHITE, dtype=np.uint8)

# Створюємо правильний шестикутник.
cx, cy = 180, 190
radius = 100

points = []

for i in range(6):
    angle = math.radians(-90 + i * 60)
    x = round(cx + radius * math.cos(angle))
    y = round(cy + radius * math.sin(angle))
    points.append((x, y))

# Заливаємо шестикутник власною функцією.
fill_polygon(img, points, BLUE)

# Малюємо контур власною функцією line.
for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % len(points)]
    line(img, x1, y1, x2, y2, BLACK)

# Додатково демонструємо заливку круга.
fill_circle(img, 180, 190, 65, RED)

# Контур круга для наочності.
for angle in range(360):
    a1 = math.radians(angle)
    a2 = math.radians(angle + 1)

    x1 = round(180 + 65 * math.cos(a1))
    y1 = round(190 + 65 * math.sin(a1))

    x2 = round(180 + 65 * math.cos(a2))
    y2 = round(190 + 65 * math.sin(a2))

    line(img, x1, y1, x2, y2, BLACK)

output_path = "out/task08.png"
cv2.imwrite(output_path, img)

print("Вершини шестикутника:", points)
print("Зображення збережено:", output_path)
