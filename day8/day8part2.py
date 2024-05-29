def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def decode_signals(patterns):
    patterns = [''.join(sorted(p)) for p in patterns]
    digit_map = {}
    segments_map = {}
    
    # Identify unique segment patterns for 1, 4, 7, 8
    for pattern in patterns:
        if len(pattern) == 2:
            digit_map[1] = pattern
        elif len(pattern) == 3:
            digit_map[7] = pattern
        elif len(pattern) == 4:
            digit_map[4] = pattern
        elif len(pattern) == 7:
            digit_map[8] = pattern

    for pattern in patterns:
        if len(pattern) == 5:
            if all(c in pattern for c in digit_map[1]):
                digit_map[3] = pattern
            elif sum(c in pattern for c in digit_map[4]) == 3:
                digit_map[5] = pattern
            else:
                digit_map[2] = pattern
        elif len(pattern) == 6:
            if all(c in pattern for c in digit_map[4]):
                digit_map[9] = pattern
            elif all(c in pattern for c in digit_map[1]):
                digit_map[0] = pattern
            else:
                digit_map[6] = pattern

    return {v: k for k, v in digit_map.items()}

def decode_output(output, digit_map):
    output = [''.join(sorted(o)) for o in output]
    return int(''.join(str(digit_map[o]) for o in output))

def calculate_output_sum(lines):
    total_sum = 0
    for line in lines:
        patterns, output = line.split(" | ")
        patterns = patterns.split()
        output = output.split()
        
        digit_map = decode_signals(patterns)
        decoded_value = decode_output(output, digit_map)
        total_sum += decoded_value
    
    return total_sum

file_path = 'input.txt'
lines = read_input(file_path)
total_sum = calculate_output_sum(lines)
print(f"Sum of all decoded output values: {total_sum}")
