with open("real-input.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)
cols = len(grid[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0), (1, 1)
]

total_removed = 0

while True:
    to_remove = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                adjacent = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == '@':
                            adjacent += 1
                if adjacent < 4:
                    to_remove.append((i, j))
    
    if not to_remove:
        break  
    
    for i, j in to_remove:
        grid[i][j] = '.'
    
    total_removed += len(to_remove)

print("Total rolls removed:", total_removed)
