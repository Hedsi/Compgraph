import numpy as np
from circle import circle

SIZE = 2 * 100 + 5
cx = SIZE // 2
cy = SIZE // 2

for r in range(1, 101):
    img = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)

    circle(img, cx, cy, r, (255, 255, 255))

    ys, xs = np.where(img[:, :, 0] == 255)

    if len(xs) == 0:
        raise AssertionError(f"Коло радіуса {r} не намальовано")

    distances = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
    errors = np.abs(distances - r)

    max_error = np.max(errors)

    if max_error >= 0.5:
        raise AssertionError(
            f"Радіус {r}: максимальна похибка {max_error:.4f} "
            f"не менша за 0.5"
        )

print("Усі кола радіусів 1–100 пройшли перевірку!")