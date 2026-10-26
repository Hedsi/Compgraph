
import os
import numpy as np
import cv2

from rounded_rectangle import draw_rounded_rectangle

os.makedirs("out", exist_ok=True)

img = np.full((400, 600, 3), 255, dtype=np.uint8)

BLACK = (0, 0, 0)
BLUE = (220, 100, 30)
RED = (30, 30, 220)
GREEN = (30, 150, 30)

# Великий прямокутник із товстим контуром.
draw_rounded_rectangle(
    img, 60, 60, 540, 340,
    radius=45, color=BLACK, thickness=3
)

# Додаткові приклади з різними радіусами.
draw_rounded_rectangle(
    img, 100, 100, 300, 180,
    radius=20, color=BLUE, thickness=2
)

draw_rounded_rectangle(
    img, 330, 120, 480, 250,
    radius=60, color=RED, thickness=2
)

draw_rounded_rectangle(
    img, 180, 230, 400, 300,
    radius=0, color=GREEN, thickness=2
)

output_path = "out/task11.png"
cv2.imwrite(output_path, img)

print(f"Зображення збережено: {output_path}")
