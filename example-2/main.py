import csv
from graph import Graph
import networkx as nx
import matplotlib.pyplot as plt

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
    max_path = []
    max_cost = -1
    
    def dfs_recursive(current: str, path: list, cost: int):
        nonlocal max_path, max_cost
        visited.add(current)
        path.append(current)
        
        if current == end:
            if cost > max_cost:
                max_cost = cost
                max_path = path.copy()
        
        current_index = graph.vertex_index[current]
        temp = graph.array[current_index].head
        while temp:
            if temp.value not in visited:
                dfs_recursive(temp.value, path, cost + temp.weight)
            temp = temp.next
        
        path.pop()
        visited.remove(current)
    
    dfs_recursive(start, [], 0)
    return max_path, max_cost

def add_edges(file_path, graph: Graph):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        for row in csv_reader:
            graph.add_edge(row[0], row[1], int(row[2]))

def draw_graph(G, pos, title, path=None, color='r'):
    plt.clf()
    plt.title(title)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=300, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=color, width=2)
    
    plt.pause(1.0)  

def animate_search(G, bfs_path, dfs_path):
    pos = nx.spring_layout(G, seed=42)
    plt.ion()
    
    # Draw DFS path
    for i in range(len(dfs_path)):
        plt.clf()
        plt.title("Busca em Profundidade (DFS) (vermelho)")
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=300, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        
        dfs_edges = list(zip(dfs_path[:i+1], dfs_path[1:i+2]))
        nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='r', width=2)
        
        plt.pause(1.0) 
    
 
    plt.clf()
    plt.title("Busca em Profundidade (DFS) (vermelho)")
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=300, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    dfs_edges = list(zip(dfs_path, dfs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='r', width=2)
    plt.pause(3.0)  
    
    # Draw BFS path
    for i in range(len(bfs_path)):
        plt.clf()
        plt.title("Busca em Largura (BFS) (azul)")
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=300, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        
        bfs_edges = list(zip(bfs_path[:i+1], bfs_path[1:i+2]))
        nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='b', width=2)
        
        plt.pause(1.0) 
    
    # Draw final BFS path
    plt.clf()
    plt.title("Busca em Largura (BFS) (azul)")
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=300, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    bfs_edges = list(zip(bfs_path, bfs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='b', width=2)
    plt.pause(2.0)  
    
    plt.ioff()
    plt.show()

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
    bfs_path_result = bfs_path(graph, start, end)
    dfs_path_result, dfs_cost = dfs_path(graph, start, end)
    print("\nCaminho BFS:", bfs_path_result)
    print("Caminho DFS:", dfs_path_result)
    print("Custo total do caminho DFS:", dfs_cost)
    
    # Convert Graph to NetworkX graph for visualization
    G = nx.DiGraph()
    for v in vertices:
        G.add_node(v)
    for v in vertices:
        current_index = graph.vertex_index[v]
        temp = graph.array[current_index].head
        while temp:
            G.add_edge(v, temp.value, weight=temp.weight)
            temp = temp.next
    
    animate_search(G, bfs_path_result, dfs_path_result)

if __name__ == "__main__":
    main()

