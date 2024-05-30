def parse_input(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def move_cucumbers(grid):
    rows = len(grid)
    cols = len(grid[0])
    moved = False
    
    # Move east-facing cucumbers
    new_grid = [row[:] for row in grid]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '>' and grid[r][(c + 1) % cols] == '.':
                new_grid[r][c] = '.'
                new_grid[r][(c + 1) % cols] = '>'
                moved = True
    grid = [row[:] for row in new_grid]

    # Move south-facing cucumbers
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'v' and grid[(r + 1) % rows][c] == '.':
                new_grid[r][c] = '.'
                new_grid[(r + 1) % rows][c] = 'v'
                moved = True

    return new_grid, moved

def simulate_until_stable(grid):
    steps = 0
    while True:
        grid, moved = move_cucumbers(grid)
        steps += 1
        if not moved:
            break
    return steps

# Example usage
file_path = 'input.txt'
grid = parse_input(file_path)
steps = simulate_until_stable(grid)
print("Number of steps to reach steady state:", steps)
