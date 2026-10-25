import random
import numpy as np
from line import line


def get_pixels(x0, y0, x1, y1):
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    line(img, x0, y0, x1, y1, (255, 255, 255))

    return {
        (x, y)
        for y in range(100)
        for x in range(100)
        if img[y, x, 0] == 255
    }



special_cases = [
    (10, 10, 10, 10),  
    (10, 10, 10, 80),  
    (10, 10, 80, 10),  
    (10, 10, 80, 40),  
    (10, 80, 80, 10),  
    (80, 10, 10, 40),  
    (80, 80, 10, 10),  
]

for x0, y0, x1, y1 in special_cases:
    assert get_pixels(x0, y0, x1, y1) == get_pixels(
        x1, y1, x0, y0
    )


for _ in range(1000):
    x0, y0 = random.randrange(100), random.randrange(100)
    x1, y1 = random.randrange(100), random.randrange(100)

    forward = get_pixels(x0, y0, x1, y1)
    backward = get_pixels(x1, y1, x0, y0)

    assert forward == backward, (
        f"Результати відрізняються: ({x0}, {y0}) -> "
        f"({x1}, {y1})"
    )

print("Усі перевірки пройдено: 1000 з 1000!")