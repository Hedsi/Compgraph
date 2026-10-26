def circle(img, cx, cy, r, color):
    if r < 0:
        raise ValueError("Радіус не може бути від'ємним")

    x = 0
    y = r
    p = 1 - r

    while x <= y:
        points = [
            (cx + x, cy + y),
            (cx - x, cy + y),
            (cx + x, cy - y),
            (cx - x, cy - y),
            (cx + y, cy + x),
            (cx - y, cy + x),
            (cx + y, cy - x),
            (cx - y, cy - x),
        ]

        for px, py in points:
            if 0 <= px < img.shape[1] and 0 <= py < img.shape[0]:
                img[py, px] = color

        x += 1

        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1