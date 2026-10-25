def line(img, x0, y0, x1, y1, color):
    if (x0, y0) > (x1, y1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy

    while True:
        if 0 <= x0 < img.shape[1] and 0 <= y0 < img.shape[0]:
            img[y0, x0] = color

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x0 += sx

        if e2 < dx:
            err += dx
            y0 += sy
def thick_line(img, A, B, color, width):
    import math

    if width < 1:
        raise ValueError("width має бути не менше 1")

    x0, y0 = A
    x1, y1 = B

    
    if width == 1:
        line(img, x0, y0, x1, y1, color)
        return

    dx = x1 - x0
    dy = y1 - y0
    length = math.sqrt(dx * dx + dy * dy)


    if length == 0:
        radius = width // 2
        for y in range(y0 - radius, y0 + radius + 1):
            for x in range(x0 - radius, x0 + radius + 1):
                if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
                    img[y, x] = color
        return


    nx = -dy / length
    ny = dx / length


    for i in range(width):
        offset = i - (width - 1) / 2
        ax = round(x0 + nx * offset)
        ay = round(y0 + ny * offset)
        bx = round(x1 + nx * offset)
        by = round(y1 + ny * offset)

        line(img, ax, ay, bx, by, color)