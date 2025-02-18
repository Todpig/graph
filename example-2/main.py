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

