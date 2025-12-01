starting_point = 50
zero_counter = 0

with open("real-input.txt", mode="r") as file:
    read_data = file.read().splitlines()

    for line in read_data:
        amount = int(line[1:])

        if line[0:1] == "R":
            for _ in range(amount):
                starting_point = (starting_point + 1) % 100
                if starting_point == 0:
                    zero_counter += 1

        if line[0:1] == "L":
            for _ in range(amount):
                starting_point = (starting_point - 1) % 100
                if starting_point == 0:
                    zero_counter += 1

print(zero_counter)