import numpy as np
from fill import fill_polygon, fill_circle

img = np.zeros((40, 50, 3), dtype=np.uint8)

points = [
    (10, 10),
    (30, 10),
    (30, 20),
    (10, 20),
]

fill_polygon(img, points, (255, 255, 255))

count = np.count_nonzero(np.any(img != 0, axis=2))

print("Кількість зафарбованих пікселів:", count)
assert count == 200, f"Очікувалося 200 пікселів, отримано {count}"

print("Тест прямокутника пройдено!")

circle_img = np.zeros((50, 50, 3), dtype=np.uint8)
fill_circle(circle_img, 25, 25, 10, (255, 255, 255))

circle_count = np.count_nonzero(np.any(circle_img != 0, axis=2))
assert circle_count > 0, "Коло не було зафарбоване"

print("Тест заливки круга пройдено!")
print("Кількість пікселів у крузі:", circle_count)