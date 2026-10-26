def fill_polygon(img, points, color):

    if len(points) < 3:
        raise ValueError("Многокутник повинен мати щонайменше 3 вершини")

    height, width = img.shape[:2]

    for y in range(height):
        scan_y = y + 0.5
        intersections = []

        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]


            if y1 == y2:
                continue


            if min(y1, y2) <= scan_y < max(y1, y2):
                x_intersection = x1 + (
                    (scan_y - y1) * (x2 - x1) / (y2 - y1)
                )
                intersections.append(x_intersection)

        intersections.sort()


        for i in range(0, len(intersections) - 1, 2):
            left = intersections[i]
            right = intersections[i + 1]

            x_start = max(0, int(__import__("math").ceil(left - 0.5)))
            x_end = min(width, int(__import__("math").ceil(right - 0.5)))

            for x in range(x_start, x_end):
                img[y, x] = color


def fill_circle(img, cx, cy, r, color):
    """Заливка круга за перевіркою центрів пікселів."""
    if r < 0:
        raise ValueError("Радіус не може бути від'ємним")

    height, width = img.shape[:2]

    for y in range(max(0, cy - r - 1), min(height, cy + r + 1)):
        dy = 2 * y + 1 - 2 * cy

        for x in range(max(0, cx - r - 1), min(width, cx + r + 1)):
            dx = 2 * x + 1 - 2 * cx

            if dx * dx + dy * dy <= (2 * r) ** 2:
                img[y, x] = color
                
def flood_fill(img, x, y, color, connectivity=4):

    if connectivity not in (4, 8):
        raise ValueError("connectivity повинен бути 4 або 8")

    height, width = img.shape[:2]

    # Перевіряємо, чи початкова точка всередині зображення.
    if not (0 <= x < width and 0 <= y < height):
        return 0

    old_color = img[y, x].copy()

    # Якщо колір не змінюється, заливати нічого не потрібно.
    if (old_color == color).all():
        return 0

    if connectivity == 4:
        neighbors = [
            (-1, 0),  # ліворуч
            (1, 0),   # праворуч
            (0, -1),  # вгору
            (0, 1)    # вниз
        ]
    else:
        neighbors = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

    stack = [(x, y)]
    filled = 0

    # Замінюємо колір одразу, щоб не додавати цей піксель
    # у стек повторно.
    img[y, x] = color

    while stack:
        px, py = stack.pop()
        filled += 1

        for dx, dy in neighbors:
            nx = px + dx
            ny = py + dy

            if not (0 <= nx < width and 0 <= ny < height):
                continue

            # Заливаємо лише пікселі початкового кольору.
            if (img[ny, nx] == old_color).all():
                img[ny, nx] = color
                stack.append((nx, ny))

    return filled
