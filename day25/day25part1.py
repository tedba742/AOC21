def parse_input(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def move_cucumbers(grid):
    rows = len(grid)
    cols = len(grid[0])
    moved = False

    new_grid = [row[:] for row in grid]
    for r in range(rows):
        for c in range(cols):
            next_c = (c + 1) % cols
            if grid[r][c] == '>' and grid[r][next_c] == '.':
                new_grid[r][c] = '.'
                new_grid[r][next_c] = '>'
                moved = True

    grid = [row[:] for row in new_grid]

    for r in range(rows):
        for c in range(cols):
            next_r = (r + 1) % rows
            if grid[r][c] == 'v' and grid[next_r][c] == '.':
                new_grid[r][c] = '.'
                new_grid[next_r][c] = 'v'
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

file_path = 'input.txt'
grid = parse_input(file_path)
steps = simulate_until_stable(grid)
print("Number of steps to reach steady state:", steps)
