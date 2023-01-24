import numpy as np

grid = np.array(
    [
        list(map(int, list(line)))
        for line in open("day8/input.txt", "r").read().strip().split()
    ]
)


total = 0
for i in range((m := len(grid))):
    for j in range((n := len(grid[0]))):
        h = grid[i, j]

        if (
            j == 0
            or np.amax(grid[i, :j]) < h # toda la fila a la izquierda
            or j == m - 1
            or np.amax(grid[i, (j + 1) :]) < h  # el que está a la derecha hasta el final
            or i == 0
            or np.amax(grid[:i, j]) < h # toda la columna en la posición j
            or i == n - 1
            or np.amax(grid[(i + 1) :, j]) < h  # toda la fila a la derecha
        ):
            total += 1

print(total)



pos = int(maps[x][y])
above, below = int(maps[x - 1][y]), int(maps[x + 1][y])
before, after = int(maps[x][y - 1]), int(maps[x][y + 1])

if (
    ()
    ((before < pos) or (above < pos))
    and ((below < pos) or (after < pos))

):
    a += 1
    print(f"row: {x} col: {y} ==> {pos}")