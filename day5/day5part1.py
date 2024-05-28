def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def parse_line(line):
    parts = line.split(' -> ')
    x1, y1 = map(int, parts[0].split(','))
    x2, y2 = map(int, parts[1].split(','))
    return x1, y1, x2, y2

def get_points_on_line(x1, y1, x2, y2):
    points = []
    if x1 == x2:  # Vertical line
        y_start, y_end = sorted([y1, y2])
        for y in range(y_start, y_end + 1):
            points.append((x1, y))
    elif y1 == y2:  # Horizontal line
        x_start, x_end = sorted([x1, x2])
        for x in range(x_start, x_end + 1):
            points.append((x, y1))
    return points

def count_overlaps(lines):
    point_counts = {}
    for line in lines:
        x1, y1, x2, y2 = parse_line(line)
        points = get_points_on_line(x1, y1, x2, y2)
        for point in points:
            if point not in point_counts:
                point_counts[point] = 0
            point_counts[point] += 1
    return sum(1 for count in point_counts.values() if count >= 2)

def main():
    lines = read_input('input.txt')
    overlap_count = count_overlaps(lines)
    print(f"The number of points where at least two lines overlap is: {overlap_count}")

if __name__ == "__main__":
    main()
