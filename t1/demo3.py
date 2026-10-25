
import os
import numpy as np

from draw import save
from hsv import rgb_to_hsv, hsv_to_rgb


def main():
    w, h = 740, 580


    img = np.zeros((h, w, 3), dtype=np.uint8)


    cx = w // 2
    cy = h // 2
    radius = min(w, h) // 2 - 10


    for y in range(h):
        for x in range(w):
            dx = x - cx
            dy = cy - y

            distance = np.sqrt(dx * dx + dy * dy)

            if distance <= radius:

                hue = np.degrees(np.arctan2(dy, dx)) % 360.0


                saturation = distance / radius


                value = 1.0

                r, g, b = hsv_to_rgb(hue, saturation, value)


                img[y, x] = (b, g, r)


    os.makedirs("out", exist_ok=True)
    save(img, "out/task03.png")

    h1, s1, v1 = rgb_to_hsv(255, 128, 0)
    print(
        f"RGB(255, 128, 0) -> "
        f"H={h1:.1f}, S={s1:.3f}, V={v1:.3f}"
    )


    h2, s2, v2 = rgb_to_hsv(128, 128, 128)
    print(
        f"RGB(128, 128, 128) -> "
        f"H={h2:.1f}, S={s2:.3f}, V={v2:.3f}"
    )


    rng = np.random.default_rng(42)
    colors = rng.integers(0, 256, size=(10000, 3))

    max_diff = 0

    for color in colors:
        r, g, b = map(int, color)

        hue, sat, val = rgb_to_hsv(r, g, b)
        r2, g2, b2 = hsv_to_rgb(hue, sat, val)

        diff = max(
            abs(r - r2),
            abs(g - g2),
            abs(b - b2)
        )

        max_diff = max(max_diff, diff)

    print(f"Максимальна різниця каналів: {max_diff}")
    print("Зображення збережено: out/task03.png")

    if max_diff <= 1:
        print("Усі 10 000 тестів пройдено!")
    else:
        print("Помилка: різниця перевищує 1.")


if __name__ == "__main__":
    main()
