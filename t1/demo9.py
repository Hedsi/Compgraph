
import os
import numpy as np
import cv2

from line import line
from fill import flood_fill

os.makedirs("out", exist_ok=True)

SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 0, 255)

for connectivity in (4, 8):
    img = np.full((SIZE, SIZE, 3), WHITE, dtype=np.uint8)


    line(img, 0, 0, 99, 99, BLACK)


    count = flood_fill(img, 90, 10, RED, connectivity)

    filename = f"out/task09{connectivity}.png"
    cv2.imwrite(filename, img)

    print(f"{connectivity}-сусідство: {count} пікселів")
    print(f"Зображення збережено: {filename}")
