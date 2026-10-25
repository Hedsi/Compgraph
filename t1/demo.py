

import os
from draw import canvas, set_pixel, save


def main():
    w, h = 740, 580

    # Створюємо біле полотно
    img = canvas(w, h, (255, 255, 255))

    # Малюємо червоний піксель у верхньому лівому куті
    set_pixel(img, 0, 0, (0, 0, 255))

    # Перевіряємо точку поза полотном
    set_pixel(img, -5, 3, (255, 0, 0))

    # Перевіряємо результат
    print("Колір пікселя (0, 0):", img[0, 0])
    print("Розмір масиву:", img.shape)

    # Зберігаємо зображення
    os.makedirs("out", exist_ok=True)
    save(img, "out/task01.png")

    print("Завдання 1 виконано!")
    print(f"Розмір полотна: {w} × {h}")
    print("Результат: out/task01.png")


if __name__ == "__main__":
    main()
