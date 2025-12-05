invalid_numbers = []

with open("real-input.txt", "r") as file:
    file_data = file.read().strip().split(",")

def is_invalid(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False  # cannot split evenly
    half = len(s) // 2
    return s[:half] == s[half:]  # check if first half equals second half

for r in file_data:
    left, right = map(int, r.split("-"))
    for n in range(left, right + 1):
        if is_invalid(n):
            invalid_numbers.append(n)

print("Invalid IDs:", invalid_numbers)
print("Sum of invalid IDs:", sum(invalid_numbers))