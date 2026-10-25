def line(img, x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0


    if dx < 0 or dy < 0 or dy > dx:
        raise ValueError(
            "Потрібно, щоб 0 <= dy <= dx"
        )

    x = x0
    y = y0
    p = 2 * dy - dx

    while x <= x1:

        if 0 <= y < img.shape[0] and 0 <= x < img.shape[1]:
            img[y, x] = color

        if p >= 0:
            y += 1
            p -= 2 * dx

        p += 2 * dy
        x += 1