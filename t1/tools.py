
from line import line


def draw_polygon(img, points, color, thickness=1):

    if len(points) < 2:
        return


    offsets = [(0, 0)]

    for d in range(1, max(1, thickness)):
        offsets.extend([(d, 0), (-d, 0), (0, d), (0, -d)])

    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]

        for ox, oy in offsets:
            line(img, x1 + ox, y1 + oy, x2 + ox, y2 + oy, color)


def draw_marker(img, point, color, size=5):

    x, y = point
    line(img, x - size, y, x + size, y, color)
    line(img, x, y - size, x, y + size, color)


def draw_grid(img, corners, n, color):

    if len(corners) != 4:
        raise ValueError("Потрібно передати рівно 4 кути")
    if n < 1:
        raise ValueError("n має бути не менше 1")

    p00, p10, p11, p01 = corners

    def interpolate(a, b, t):
        x = round(a[0] + (b[0] - a[0]) * t)
        y = round(a[1] + (b[1] - a[1]) * t)
        return x, y


    for i in range(n + 1):
        t = i / n
        start = interpolate(p00, p10, t)
        end = interpolate(p01, p11, t)
        line(img, start[0], start[1], end[0], end[1], color)


    for j in range(n + 1):
        t = j / n
        start = interpolate(p00, p01, t)
        end = interpolate(p10, p11, t)
        line(img, start[0], start[1], end[0], end[1], color)


def put_number(img, point, k, color):

    if not isinstance(k, int) or not 0 <= k <= 9:
        raise ValueError("k має бути цілим числом від 0 до 9")

    x, y = point
    w, h = 12, 20

    segments = {
        "a": ((x, y), (x + w, y)),
        "b": ((x + w, y), (x + w, y + h // 2)),
        "c": ((x + w, y + h // 2), (x + w, y + h)),
        "d": ((x, y + h), (x + w, y + h)),
        "e": ((x, y + h // 2), (x, y + h)),
        "f": ((x, y), (x, y + h // 2)),
        "g": ((x, y + h // 2), (x + w, y + h // 2)),
    }

    digits = {
        0: "abcdef",
        1: "bc",
        2: "abged",
        3: "abgcd",
        4: "fgbc",
        5: "afgcd",
        6: "afgecd",
        7: "abc",
        8: "abcdefg",
        9: "abfgcd",
    }

    for segment in digits[k]:
        (x1, y1), (x2, y2) = segments[segment]
        line(img, x1, y1, x2, y2, color)
