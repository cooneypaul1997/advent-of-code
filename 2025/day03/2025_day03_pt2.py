with open("real-input.txt", "r") as file:
    file_data = file.read().splitlines()
    jolt_list = []

    for line in file_data:
        k = 12
        remaining = k
        start = 0
        n = len(line)
        result = ""

        while remaining > 0:
            end = n - remaining + 1
            best_idx = max(range(start, end), key=lambda i: int(line[i]))
            result += line[best_idx]
            start = best_idx + 1
            remaining -= 1

        jolt_list.append(int(result))

total_output = sum(jolt_list)

print("Maximum joltage per bank:", jolt_list)
print("Total output joltage:", total_output)