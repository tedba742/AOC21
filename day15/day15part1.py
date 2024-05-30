import heapq

def read_input(file_path):
    with open(file_path, 'r') as file:
        grid = [list(map(int, list(line.strip()))) for line in file]
    return grid

def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(0, 0, 0)]  # (risk, row, col)
    visited = set()
    min_risk = {(0, 0): 0}

    while pq:
        current_risk, r, c = heapq.heappop(pq)
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if r == rows - 1 and c == cols - 1:
            return current_risk

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                new_risk = current_risk + grid[nr][nc]
                if (nr, nc) not in min_risk or new_risk < min_risk[(nr, nc)]:
                    min_risk[(nr, nc)] = new_risk
                    heapq.heappush(pq, (new_risk, nr, nc))

    return float('inf')

def main(file_path):
    grid = read_input(file_path)
    lowest_risk = dijkstra(grid)
    print(f"Lowest total risk: {lowest_risk}")

file_path = 'input.txt'
main(file_path)