#include <iostream>
using namespace std;

struct Node {
    int value;     
    Node* next;     
};

struct List {
    Node* head;     
};

class Graph {
private:
    List* array;    
    int numVertices;
    
public:
    Graph(int vertices) {
        numVertices = vertices;
        array = new List[vertices];
        for (int i = 0; i < vertices; i++) {
            array[i].head = NULL;
        }
    }
    
    void addVertex(int v) {
        if (v >= numVertices) {
            List* newArray = new List[v + 1];
            for (int i = 0; i < numVertices; i++) {
                newArray[i] = array[i];
            }
            
            for (int i = numVertices; i <= v; i++) {
                newArray[i].head = NULL;
            }
            
            delete[] array;
            array = newArray;
            numVertices = v + 1;
        }
    }
    
    void addEdge(int v1, int v2) {
        if (v1 >= numVertices) addVertex(v1);
        if (v2 >= numVertices) addVertex(v2);
        
        Node* newNode = new Node;
        newNode->value = v2;
        newNode->next = array[v1].head;
        array[v1].head = newNode;
        
        newNode = new Node;
        newNode->value = v1;
        newNode->next = array[v2].head;
        array[v2].head = newNode;
    }
    
    void printGraph() {
        for (int i = 0; i < numVertices; i++) {
            cout << "Vértice " << i << endl;
            Node* temp = array[i].head;
            while (temp) {
                cout << " -> " << temp->value;
                temp = temp->next;
            }
            cout << endl;
        }
    }
};

int main() {
    
    Graph graph(5);
    graph.addEdge(0, 1);
    graph.addEdge(0, 4);
    graph.addEdge(1, 2);
    graph.addEdge(1, 3);
    graph.addEdge(1, 4);
    graph.addEdge(2, 3);
    graph.addEdge(3, 4);
    graph.addEdge(4, 5);
    
    
    cout << "Estrutura do grafo:" << endl;
    graph.printGraph();
    
    return 0;
}