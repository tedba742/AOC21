from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split('-') for line in lines]

def build_graph(connections):
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def is_small_cave(cave):
    return cave.islower()

def find_all_paths(graph, start, end, path, visited, small_cave_twice):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node == 'start':
            continue
        if is_small_cave(node):
            if visited[node] == 0:
                new_visited = visited.copy()
                new_visited[node] += 1
                newpaths = find_all_paths(graph, node, end, path, new_visited, small_cave_twice)
                paths.extend(newpaths)
            elif visited[node] == 1 and not small_cave_twice:
                new_visited = visited.copy()
                new_visited[node] += 1
                newpaths = find_all_paths(graph, node, end, path, new_visited, True)
                paths.extend(newpaths)
        else:
            newpaths = find_all_paths(graph, node, end, path, visited, small_cave_twice)
            paths.extend(newpaths)
    return paths

def count_paths(graph, start, end):
    visited = defaultdict(int)
    paths = find_all_paths(graph, start, end, [], visited, False)
    return len(paths)

file_path = 'input.txt'
connections = read_input(file_path)
graph = build_graph(connections)
total_paths = count_paths(graph, 'start', 'end')
print(f"Total number of distinct paths: {total_paths}")
