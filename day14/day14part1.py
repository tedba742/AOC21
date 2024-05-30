from collections import defaultdict, Counter

# Function to read the input file
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    template = lines[0]
    rules = {}
    for line in lines[1:]:
        if '->' in line:
            pair, insert = line.split(' -> ')
            rules[pair] = insert
    return template, rules

def polymerize(template, rules, steps):
    pair_counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair_counts[template[i:i+2]] += 1
    
    for _ in range(steps):
        new_pair_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            if pair in rules:
                insert = rules[pair]
                new_pair_counts[pair[0] + insert] += count
                new_pair_counts[insert + pair[1]] += count
            else:
                new_pair_counts[pair] += count
        pair_counts = new_pair_counts

    element_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        element_counts[pair[0]] += count
    element_counts[template[-1]] += 1
    
    return element_counts

def find_difference(element_counts):
    counts = element_counts.values()
    return max(counts) - min(counts)

def main(file_path):
    template, rules = read_input(file_path)
    element_counts = polymerize(template, rules, 10)
    difference = find_difference(element_counts)
    print(difference)

file_path = 'input.txt'
main(file_path)
