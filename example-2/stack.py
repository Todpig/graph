class Node:
    def __init__(self, value: int, next: 'Node' = None):
        self.value = value
        self.next = next         

class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, value: int):
        if(self.head == None):
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
    def print_stack(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next