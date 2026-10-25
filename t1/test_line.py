import numpy as np
from line import line


img = np.zeros((10, 20, 3), dtype=np.uint8)


line(img, 2, 2, 13, 5, (0, 0, 255))


expected_y = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]


for x, y in zip(range(2, 14), expected_y):
    assert tuple(img[y, x]) == (0, 0, 255), (
        f"Помилка: піксель ({x}, {y}) не зафарбований"
    )

print("Усі очікувані пікселі перевірено!")