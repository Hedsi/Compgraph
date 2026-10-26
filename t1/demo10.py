
import os
import numpy as np
import cv2

from tools import draw_polygon, draw_marker, draw_grid, put_number

os.makedirs("out", exist_ok=True)

img = np.full((400, 500, 3), 255, dtype=np.uint8)

BLACK = (0, 0, 0)
BLUE = (220, 100, 30)
RED = (30, 30, 220)
GREEN = (30, 150, 30)


corners = [
    (100, 70),   # 0 — верхній лівий
    (390, 110),  # 1 — верхній правий
    (350, 320),  # 2 — нижній правий
    (60, 270),   # 3 — нижній лівий
]


draw_grid(img, corners, 4, BLUE)
draw_polygon(img, corners, BLACK, thickness=2)

number_positions = [
    (corners[0][0] - 22, corners[0][1] - 28),
    (corners[1][0] + 8, corners[1][1] - 10),
    (corners[2][0] + 8, corners[2][1] - 10),
    (corners[3][0] - 22, corners[3][1] - 10),
]

for i, point in enumerate(corners):
    draw_marker(img, point, RED, size=6)
    put_number(img, number_positions[i], i, GREEN)

output_path = "out/task10.png"
cv2.imwrite(output_path, img)

print(f"Зображення збережено: {output_path}")
