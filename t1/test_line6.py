import numpy as np
import cv2

from line import line


test_lines = [
    ((2, 2), (13, 5)),       # приклад із лекції
    ((5, 5), (25, 15)),      # пологий нахил
    ((10, 30), (35, 12)),    # лінія вгору
    ((5, 5), (5, 25)),       # вертикальна лінія
    ((5, 15), (30, 15)),     # горизонтальна лінія
]

SIZE = 50

print("Порівняння line() та cv2.line()")
print("-" * 65)
print(f"{'Початок':<15} {'Кінець':<15} {'Відмінних пікселів':>20}")
print("-" * 65)

results = []

for A, B in test_lines:

    ours = np.zeros((SIZE, SIZE), dtype=np.uint8)
    opencv = np.zeros((SIZE, SIZE), dtype=np.uint8)


    line(ours, A[0], A[1], B[0], B[1], 255)


    cv2.line(opencv, A, B, 255, 1)


    different = np.count_nonzero(ours != opencv)
    results.append(different)

    print(f"{str(A):<15} {str(B):<15} {different:>20}")

print("-" * 65)

print("Збіг для прикладу з лекції:",
      "ТАК" if results[0] == 0 else "НІ")

print("Усього тестів:", len(test_lines))
print("Тестів без розбіжностей:",
      sum(value == 0 for value in results))