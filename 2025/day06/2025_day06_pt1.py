columns = []
results = []
final_result = 0

with open("real-input.txt", "r") as file:
    for line in file:
        parts = line.split()

        while len(columns) < len(parts):
            columns.append([])

        for i, part in enumerate(parts):
            columns[i].append(part)

print(f"{columns}")

for column in columns:
    *nums, op = column
    nums = list(map(int, nums))

    if op == "*":
        result = 1
        for n in nums:
            result *= n
        
        results.append(result)

    if op == "+":
        result = 0
        for n in nums:
            result += n
        
        results.append(result)

final_result = sum(results)

print(f"{final_result}")