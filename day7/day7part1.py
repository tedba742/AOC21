import statistics

def read_positions_from_file(file_path):
    with open(file_path, 'r') as file:
        positions = list(map(int, file.read().strip().split(',')))
    return positions

def calculate_fuel_cost(positions, align_position):
    return sum(abs(pos - align_position) for pos in positions)

def find_optimal_alignment(file_path):
    positions = read_positions_from_file(file_path)
    median_position = int(statistics.median(positions))
    total_fuel_cost = calculate_fuel_cost(positions, median_position)
    return median_position, total_fuel_cost


file_path = 'input.txt'
median_position, total_fuel_cost = find_optimal_alignment(file_path)
print(f"Optimal alignment position: {median_position}")
print(f"Total fuel cost: {total_fuel_cost}")
