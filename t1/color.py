
import numpy as np


GAMMA = 2.2


def to_linear(v):

    v = np.asarray(v, dtype=np.float64)
    v = np.clip(v, 0, 255) / 255.0
    return v ** GAMMA


def to_srgb(l):

    l = np.asarray(l, dtype=np.float64)
    l = np.clip(l, 0.0, 1.0)

    # Використовуємо відкидання дробової частини,
    # щоб результати відповідали прикладам завдання.
    return np.clip(255.0 * l ** (1.0 / GAMMA), 0, 255).astype(np.uint8)


def mix_colors(color1, color2):

    c1 = np.asarray(color1, dtype=np.float64)
    c2 = np.asarray(color2, dtype=np.float64)

    linear1 = to_linear(c1)
    linear2 = to_linear(c2)

    average = (linear1 + linear2) / 2.0

    return to_srgb(average)
