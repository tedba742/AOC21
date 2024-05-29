def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def count_unique_digits(lines):
    unique_lengths = {2, 3, 4, 7}  # lengths corresponding to 1, 7, 4, 8
    count = 0

    for line in lines:
        patterns, output = line.split(" | ")
        output_values = output.split()

        for value in output_values:
            if len(value) in unique_lengths:
                count += 1

    return count

file_path = 'input.txt'
lines = read_input(file_path)
unique_digit_count = count_unique_digits(lines)
print(f"Number of times digits 1, 4, 7, or 8 appear: {unique_digit_count}")
