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
                return error_score[char], None
    return 0, stack

def calculate_syntax_error_score(lines):
    total_score = 0
    incomplete_lines = []
    for line in lines:
        score, stack = find_first_illegal_character(line)
        total_score += score
        if score == 0 and stack is not None:
            incomplete_lines.append((line, stack))
    return total_score, incomplete_lines

def calculate_completion_score(stack):
    completion_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    score = 0
    while stack:
        char = stack.pop()
        score = score * 5 + completion_score[char]
    return score

def find_middle_score(incomplete_lines):
    scores = [calculate_completion_score(stack) for _, stack in incomplete_lines]
    scores.sort()
    middle_index = len(scores) // 2
    return scores[middle_index]

file_path = 'input.txt'
lines = read_input(file_path)
total_syntax_error_score, incomplete_lines = calculate_syntax_error_score(lines)
print(f"Total syntax error score: {total_syntax_error_score}")

middle_score = find_middle_score(incomplete_lines)
print(f"Middle score of the completion strings: {middle_score}")
