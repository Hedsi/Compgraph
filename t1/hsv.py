
import math


def rgb_to_hsv(r, g, b):

    r = r / 255.0
    g = g / 255.0
    b = b / 255.0

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin


    v = cmax


    if cmax == 0:
        s = 0.0
    else:
        s = delta / cmax


    if delta == 0:
        h = 0.0
    elif cmax == r:
        h = 60.0 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60.0 * (((b - r) / delta) + 2)
    else:
        h = 60.0 * (((r - g) / delta) + 4)

    return h, s, v


def hsv_to_rgb(h, s, v):

    h = h % 360.0
    s = max(0.0, min(1.0, s))
    v = max(0.0, min(1.0, v))


    if s == 0:
        value = int(round(v * 255))
        return value, value, value

    h_sector = h / 60.0
    i = int(math.floor(h_sector))
    f = h_sector - i

    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))

    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q

    return (
        int(round(r * 255)),
        int(round(g * 255)),
        int(round(b * 255))
    )
