def read_heightmap(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [[int(height) for height in line.strip()] for line in lines]

def is_low_point(heightmap, x, y):
    current_height = heightmap[x][y]
    adjacent_points = [
        (x-1, y), (x+1, y),
        (x, y-1), (x, y+1)
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

def flood_fill_basin(heightmap, x, y, visited):
    stack = [(x, y)]
    basin_size = 0
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        basin_size += 1
        for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
            if 0 <= nx < len(heightmap) and 0 <= ny < len(heightmap[0]) and (nx, ny) not in visited:
                if heightmap[nx][ny] != 9:
                    stack.append((nx, ny))
    return basin_size

def find_basins(heightmap, low_points):
    basins = []
    visited = set()
    for x, y in low_points:
        if (x, y) not in visited:
            basin_size = flood_fill_basin(heightmap, x, y, visited)
            basins.append(basin_size)
    return basins

def find_three_largest_basins_product(basins):
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]

file_path = 'input.txt'
heightmap = read_heightmap(file_path)
low_points = find_low_points(heightmap)
total_risk_level = calculate_risk_levels(heightmap, low_points)

basins = find_basins(heightmap, low_points)
largest_basins_product = find_three_largest_basins_product(basins)
print(f"Product of the sizes of the three largest basins: {largest_basins_product}")
