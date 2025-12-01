starting_point = 50
zero_counter = 0

with open("real-input.txt", mode="r") as file:
    read_data = file.read().splitlines()

    for line in read_data:
        if line[0:1] == "L":
            move_amount = int(line[1:])
            starting_point = (starting_point - move_amount) % 100

            if starting_point == 0:
                zero_counter += 1

        if line[0:1] == "R":
            move_amount = int(line[1:])
            starting_point = (starting_point + move_amount) % 100

            if starting_point == 0:
                zero_counter += 1

print(f"{zero_counter}")