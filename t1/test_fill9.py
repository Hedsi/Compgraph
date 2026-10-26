
import numpy as np

from line import line
from fill import flood_fill

SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 0, 255)


def test_flood_fill():

    img4 = np.full((SIZE, SIZE, 3), WHITE, dtype=np.uint8)
    line(img4, 0, 0, 99, 99, BLACK)

    count4 = flood_fill(img4, 90, 10, RED, 4)
    assert count4 == 4950, f"Очікувалося 4950, отримано {count4}"


    img8 = np.full((SIZE, SIZE, 3), WHITE, dtype=np.uint8)
    line(img8, 0, 0, 99, 99, BLACK)

    count8 = flood_fill(img8, 90, 10, RED, 8)
    assert count8 == 9900, f"Очікувалося 9900, отримано {count8}"

    print("Усі тести пройдено!")
    print(f"4-сусідство: {count4} пікселів")
    print(f"8-сусідство: {count8} пікселів")


if __name__ == "__main__":
    test_flood_fill()
