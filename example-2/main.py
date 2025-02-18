import csv
from graph import Graph

def get_vertices(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        vertices = set()
        for row in csv_reader:
            vertices.add(row[0])
            vertices.add(row[1])
    return list(vertices)

def bfs_better_path(graph: Graph, start, end):
    queue = []
    queue.append(start)
    visited = set()
    visited.add(start)
    count = 0
    while not queue.empty():
        current = queue.pop(0)
        count += 1
        if current == end:
            return count
        for neighbor in graph.array[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def add_edges(file_path, graph: Graph):
    with open(file_path, 'r') as file:
        vertices = set()
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        for row in csv_reader:
            graph.add_edge(row[0], row[1], int(row[2]))

def main():
    vertices = get_vertices("file.csv")
    print("Vertices: ")
    print(vertices )
    graph = Graph(vertices)
    add_edges("file.csv",graph )
    print("Grafo: ")
    graph.print_graph()
if __name__ == "__main__":
    main()

