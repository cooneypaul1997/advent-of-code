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

dp = [ [0] * cols for _ in range(rows) ]
dp[0][start_col] = 1

for r in range(rows - 1):
    for c in range(cols):
        count = dp[r][c]
        if count == 0:
            continue

        cell = grid[r + 1][c]

        if cell == ".":
            dp[r + 1][c] += count

        elif cell == "^":
            if c - 1 >= 0:
                dp[r + 1][c - 1] += count
            if c + 1 < cols:
                dp[r + 1][c + 1] += count

# All timelines that made it to the bottom row
timelines = sum(dp[rows - 1])

print(timelines)
