import numpy as np
import cv2

from line import line


img = np.full((580, 740, 3), 255, dtype=np.uint8)


line(img, 2, 2, 13, 5, (0, 0, 255))


cv2.imwrite("out/task04.png", img)

print("Зображення збережено: out/task04.png")