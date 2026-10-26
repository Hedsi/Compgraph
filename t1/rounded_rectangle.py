
import math
from line import line


def draw_rounded_rectangle(img, x1, y1, x2, y2, radius, color, thickness=1):

    height, width = img.shape[:2]

    if x1 > x2 or y1 > y2:
        raise ValueError("Некоректні координати прямокутника")
    if radius < 0:
        raise ValueError("Радіус не може бути від'ємним")
    if thickness < 1:
        raise ValueError("Товщина має бути не менше 1")
    if not (0 <= x1 < width and 0 <= x2 < width and
            0 <= y1 < height and 0 <= y2 < height):
        raise ValueError("Прямокутник має бути в межах зображення")

    radius = min(radius, (x2 - x1) // 2, (y2 - y1) // 2)

    def draw_outline(left, top, right, bottom, r):

        centers = [
            (right - r, top + r, -90, 0),    # верхній правий
            (right - r, bottom - r, 0, 90),  # нижній правий
            (left + r, bottom - r, 90, 180), # нижній лівий
            (left + r, top + r, 180, 270),   # верхній лівий
        ]

        points = []

        if r == 0:
            points = [
                (left, top),
                (right, top),
                (right, bottom),
                (left, bottom),
            ]
        else:

            for cx, cy, start_angle, end_angle in centers:
                for angle in range(start_angle, end_angle + 1, 5):
                    rad = math.radians(angle)
                    px = round(cx + r * math.cos(rad))
                    py = round(cy + r * math.sin(rad))
                    points.append((px, py))


                rad = math.radians(end_angle)
                points.append((
                    round(cx + r * math.cos(rad)),
                    round(cy + r * math.sin(rad))
                ))


        for i in range(len(points)):
            ax, ay = points[i]
            bx, by = points[(i + 1) % len(points)]
            line(img, ax, ay, bx, by, color)


    for offset in range(thickness):
        left = x1 + offset
        top = y1 + offset
        right = x2 - offset
        bottom = y2 - offset

        if left >= right or top >= bottom:
            break

        r = max(0, radius - offset)
        r = min(r, (right - left) // 2, (bottom - top) // 2)

        draw_outline(left, top, right, bottom, r)
