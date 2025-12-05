numbers = []
repeating_numbers = []

def is_repeating(num):
    s = str(num)
    slen = len(s)
    for i in range(1, slen):
        pattern = s[:i]
        if slen % i == 0 and s == pattern * (slen // i):
            return True   # just return True/False for easier use
    return False

with open("real-input.txt", "r") as file:
    file_data = file.read().strip().split(",")

    for r in file_data:
        left, right = map(int, r.split("-"))
        for n in range(left, right + 1):
            numbers.append(n)
            if is_repeating(n):
                repeating_numbers.append(n)

print("Repeating numbers:", repeating_numbers)
print("Sum of repeating numbers:", sum(repeating_numbers))
