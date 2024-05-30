def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [[int(char) for char in line.strip()] for line in lines]

def increase_energy(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] += 1

def flash(grid, flashed, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not flashed[nx][ny]:
            grid[nx][ny] += 1

def process_flashes(grid, flashed):
    flash_occurred = True
    while flash_occurred:
        flash_occurred = False
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] > 9 and not flashed[x][y]:
                    flash_occurred = True
                    flashed[x][y] = True
                    flash(grid, flashed, x, y)

def reset_flashed(grid, flashed):
    flash_count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if flashed[x][y]:
                grid[x][y] = 0
                flash_count += 1
                flashed[x][y] = False
    return flash_count

def simulate_steps(grid, steps):
    total_flashes = 0
    for _ in range(steps):
        flashed = [[False] * len(grid[0]) for _ in range(len(grid))]
        increase_energy(grid)
        process_flashes(grid, flashed)
        total_flashes += reset_flashed(grid, flashed)
    return total_flashes

file_path = 'input.txt'
grid = read_input(file_path)
steps = 100
total_flashes = simulate_steps(grid, steps)
print(f"Total flashes after {steps} steps: {total_flashes}")
