
import numpy as np
import cv2


def canvas(w, h, color):
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img[:, :] = color
    return img


def set_pixel(img, x, y, color):
    h, w = img.shape[:2]

    if 0 <= x < w and 0 <= y < h:
        img[y, x] = color


def save(img, path):
    if not cv2.imwrite(path, img):
        raise IOError(f"Не вдалося зберегти зображення: {path}")
