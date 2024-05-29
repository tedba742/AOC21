def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def find_first_illegal_character(line):
    matching_brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    error_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    stack = []
    
    for char in line:
        if char in matching_brackets:
            stack.append(matching_brackets[char])
        elif char in matching_brackets.values():
            if not stack or char != stack.pop():
                return error_score[char]
    return 0

def calculate_syntax_error_score(lines):
    total_score = 0
    for line in lines:
        total_score += find_first_illegal_character(line)
    return total_score

file_path = 'input.txt'
lines = read_input(file_path)
total_syntax_error_score = calculate_syntax_error_score(lines)
print(f"Total syntax error score: {total_syntax_error_score}")
