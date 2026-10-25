
import os
import numpy as np

from draw import save
from color import to_linear, to_srgb, mix_colors


def main():
    w, h = 740, 580
    half_h = h // 2


    img = np.zeros((h, w, 3), dtype=np.uint8)


    levels = np.minimum(
        np.arange(w) * 256 // w,
        255
    ).astype(np.uint8)


    img[:half_h, :, 0] = levels
    img[:half_h, :, 1] = levels
    img[:half_h, :, 2] = levels


    linear_levels = levels.astype(np.float64) / 255.0
    srgb_levels = to_srgb(linear_levels)

    img[half_h:, :, 0] = srgb_levels
    img[half_h:, :, 1] = srgb_levels
    img[half_h:, :, 2] = srgb_levels


    print("Лінійна яскравість чорного:", to_linear(0))
    print("Лінійна яскравість білого:", to_linear(255))

    print(
        "Суміш чорного й білого:",
        mix_colors([0, 0, 0], [255, 255, 255])
    )

    four_pixels = np.array([0, 0, 0, 255], dtype=np.float64)
    average_linear = np.mean(to_linear(four_pixels))
    print("Середнє чотирьох пікселів:", to_srgb(average_linear))


    os.makedirs("out", exist_ok=True)
    save(img, "out/task02.png")

    print(f"Розмір зображення: {w} × {h}")
    print("Збережено: out/task02.png")


if __name__ == "__main__":
    main()
