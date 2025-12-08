with open("real-input.txt", "r") as file:
    grid = file.read().splitlines()

rows = len(grid)
cols = len(grid[0])
accessible_count = 0

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '@':
            adjacent_rolls = 0
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == '@':
                        adjacent_rolls += 1
            if adjacent_rolls < 4:
                accessible_count += 1

print("Accessible rolls:", accessible_count)
