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

def find_all_paths(graph, start, end, path):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path or not is_small_cave(node):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def count_paths(graph, start, end):
    paths = find_all_paths(graph, start, end, [])
    return len(paths)

file_path = 'input.txt'
connections = read_input(file_path)
graph = build_graph(connections)
total_paths = count_paths(graph, 'start', 'end')
print(f"Total number of distinct paths: {total_paths}")
