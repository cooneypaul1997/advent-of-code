with open("real-input.txt", "r") as f:
    content = f.read().splitlines()

# Stop at blank line
blank_index = content.index("")
range_lines = content[:blank_index]

# Parse ranges as tuples (start, end)
ranges = [tuple(map(int, line.split("-"))) for line in range_lines]

# Sort ranges by start
ranges.sort()

merged = []
for start, end in ranges:
    if not merged:
        merged.append([start, end])
    else:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # overlap or contiguous
            merged[-1][1] = max(last_end, end)  # merge
        else:
            merged.append([start, end])

# Sum the total number of unique IDs
total_fresh = sum(end - start + 1 for start, end in merged)
print("Total fresh ingredient IDs:", total_fresh)
