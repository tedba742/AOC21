def read_heightmap(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [[int(height) for height in line.strip()] for line in lines]

def is_low_point(heightmap, x, y):
    current_height = heightmap[x][y]
    adjacent_points = [
        (x-1, y), (x+1, y),  # up, down
        (x, y-1), (x, y+1)   # left, right
    ]
    
    for i, j in adjacent_points:
        if 0 <= i < len(heightmap) and 0 <= j < len(heightmap[0]):
            if heightmap[i][j] <= current_height:
                return False
    return True

def find_low_points(heightmap):
    low_points = []
    for x in range(len(heightmap)):
        for y in range(len(heightmap[0])):
            if is_low_point(heightmap, x, y):
                low_points.append((x, y))
    return low_points

def calculate_risk_levels(heightmap, low_points):
    risk_levels = [heightmap[x][y] + 1 for x, y in low_points]
    return sum(risk_levels)

file_path = 'input.txt'
heightmap = read_heightmap(file_path)
low_points = find_low_points(heightmap)
total_risk_level = calculate_risk_levels(heightmap, low_points)
print(f"Sum of the risk levels of all low points: {total_risk_level}")