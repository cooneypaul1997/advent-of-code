# Read the file
with open("real-input.txt", "r") as f:
    content = f.read().splitlines()

# Split at the blank line
blank_index = content.index("")
range_lines = content[:blank_index]
id_lines = content[blank_index + 1:]

# Parse the ranges
ranges = []
for line in range_lines:
    start, end = map(int, line.split("-"))
    ranges.append((start, end))

# Parse available ingredient IDs
available_ids = [int(line) for line in id_lines]

# Count fresh IDs
fresh_count = 0
for id_ in available_ids:
    if any(start <= id_ <= end for start, end in ranges):
        fresh_count += 1

print("Number of fresh ingredients:", fresh_count)
