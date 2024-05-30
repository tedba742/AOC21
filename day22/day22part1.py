def parse_input(file_path):
    steps = []
    with open(file_path, 'r') as file:
        for line in file:
            action, ranges = line.strip().split(' ')
            x_range, y_range, z_range = ranges.split(',')
            x_start, x_end = map(int, x_range[2:].split('..'))
            y_start, y_end = map(int, y_range[2:].split('..'))
            z_start, z_end = map(int, z_range[2:].split('..'))
            steps.append((action, x_start, x_end, y_start, y_end, z_start, z_end))
    return steps

def apply_steps(steps, region_limit):
    cubes = set()
    
    for action, x_start, x_end, y_start, y_end, z_start, z_end in steps:
        if x_end < -region_limit or x_start > region_limit or y_end < -region_limit or y_start > region_limit or z_end < -region_limit or z_start > region_limit:
            continue
        
        x_start = max(x_start, -region_limit)
        x_end = min(x_end, region_limit)
        y_start = max(y_start, -region_limit)
        y_end = min(y_end, region_limit)
        z_start = max(z_start, -region_limit)
        z_end = min(z_end, region_limit)
        
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                for z in range(z_start, z_end + 1):
                    if action == 'on':
                        cubes.add((x, y, z))
                    else:
                        cubes.discard((x, y, z))
    
    return len(cubes)

# Example usage
file_path = 'input.txt'
steps = parse_input(file_path)
region_limit = 50
num_cubes_on = apply_steps(steps, region_limit)
print("Number of cubes that are on:", num_cubes_on)
