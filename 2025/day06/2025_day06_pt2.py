columns = []
results = []
final_result = 0

# Read file as raw lines
with open("real-input.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]

# Pad all lines to same width
width = max(len(line) for line in lines)
padded = [line.ljust(width) for line in lines]

# Build columns right-to-left, top-to-bottom
for col in range(width - 1, -1, -1):
    column = [row[col] for row in padded]
    columns.append(column)

# Split columns into problems separated by blank columns
problems = []
current = []

for col in columns:
    if all(c == " " for c in col):      # separator column
        if current:
            problems.append(current)
            current = []
    else:
        current.append(col)

if current:
    problems.append(current)

# Solve each problem
for problem in problems:
    # operator is last row, last non-space char
    op = None
    for col in reversed(problem):
        if col[-1].strip():
            op = col[-1]
            break

    nums = []
    for col in problem:
        # build number from column digits (exclude last row with operator)
        number_digits = [c for c in col[:-1] if c.strip()]
        if number_digits:
            number = int("".join(number_digits))
            nums.append(number)

    if op == "*":
        result = 1
        for n in nums:
            result *= n
    else:
        result = sum(nums)

    results.append(result)

final_result = sum(results)
print(final_result)
