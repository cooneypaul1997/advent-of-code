file_path = r"C:\Vibing\advent-of-code\2025\day07\real-input.txt"

with open(file_path) as f:
    grid = f.read().splitlines()

rows = len(grid)
cols = len(grid[0])

# Find S
for c in range(cols):
    if grid[0][c] == "S":
        start_col = c
        break

# Active beams are (row, col)
beams = {(0, start_col)}
splits = 0

while beams:
    new_beams = set()

    for r, c in beams:
        nr = r + 1

        if nr >= rows:
            continue

        cell = grid[nr][c]

        if cell == ".":
            new_beams.add((nr, c))

        elif cell == "^":
            splits += 1

            if c - 1 >= 0:
                new_beams.add((nr, c - 1))

            if c + 1 < cols:
                new_beams.add((nr, c + 1))

    beams = new_beams

print(splits)