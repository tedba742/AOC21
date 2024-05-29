def read_positions_from_file(file_path):
    with open(file_path, 'r') as file:
        positions = list(map(int, file.read().strip().split(',')))
    return positions

def calculate_progressive_fuel_cost(distance):
    return distance * (distance + 1) // 2

def total_fuel_cost_for_position(positions, target_position):
    return sum(calculate_progressive_fuel_cost(abs(pos - target_position)) for pos in positions)

def find_optimal_alignment(file_path):
    positions = read_positions_from_file(file_path)
    min_position = min(positions)
    max_position = max(positions)
    
    min_fuel_cost = float('inf')
    best_position = None
    
    for position in range(min_position, max_position + 1):
        current_fuel_cost = total_fuel_cost_for_position(positions, position)
        if current_fuel_cost < min_fuel_cost:
            min_fuel_cost = current_fuel_cost
            best_position = position
    
    return best_position, min_fuel_cost

file_path = 'input.txt'
median_position, total_fuel_cost = find_optimal_alignment(file_path)
print(f"Optimal alignment position: {median_position}")
print(f"Total fuel cost: {total_fuel_cost}")
