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

def bfs_path(graph: Graph, start: str, end: str):
    queue = []
    queue.append(start)
    visited = set()
    visited.add(start)
    parent = {start: None}
    
    while queue:
        current = queue.pop(0)
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        current_index = graph.vertex_index[current]
        temp = graph.array[current_index].head
        while temp:
            if temp.value not in visited:
                visited.add(temp.value)
                queue.append(temp.value)
                parent[temp.value] = current
            temp = temp.next
    return None

def dfs_path(graph: Graph, start: str, end: str):
    visited = set()
    path = []
    dfs_recursive(start, visited, path, graph, end)
    return path if path and path[-1] == end else None

def dfs_recursive(current: str, visited: set, path: list, graph: Graph, end: str):
        visited.add(current)
        path.append(current)
        
        if current == end:
            return True
            
        current_index = graph.vertex_index[current]
        temp = graph.array[current_index].head
        while temp:
            if temp.value not in visited:
                if dfs_recursive(temp.value, visited, path, graph, end):
                    return True
            temp = temp.next
        
        path.pop()
        return False

def add_edges(file_path, graph: Graph):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        for row in csv_reader:
            graph.add_edge(row[0], row[1], int(row[2]))

def main():
    vertices = get_vertices("file.csv")
    print("Vertices: ")
    print(vertices)
    graph = Graph(vertices)
    add_edges("file.csv", graph)
    print("Grafo: ")
    graph.print_graph()
    
    start = input("Digite o vértice de início: ").upper()
    end = input("Digite o vértice de destino: ").upper()
    if(start not in vertices or end not in vertices):
       return print("Os vértices informados não existem no grafo.")
    print("\nCaminho BFS:", bfs_path(graph, start, end))
    print("Caminho DFS:", dfs_path(graph, start, end))

if __name__ == "__main__":
    main()

