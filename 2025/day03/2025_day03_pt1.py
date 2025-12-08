with open("real-input.txt", "r") as file:
    file_data = file.read().splitlines()
    jolt_list = []

    for line in file_data:
        max_jolt = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                num = int(line[i] + line[j])
                if num > max_jolt:
                    max_jolt = num
        jolt_list.append(max_jolt)

total_output = sum(jolt_list)

print("Maximum joltage per bank:", jolt_list)
print("Total output joltage:", total_output)