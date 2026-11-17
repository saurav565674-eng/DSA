# Reverse queue using stack
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            popped_data
            print("Popped element: ",temp.data)
            self.top=self.top.next

    def print(self):
        temp = self.top
        print("stack elements are")
        while temp:
            print(temp.data)
            temp = temp.next

class LQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        if self.front:
            temp = self.front
            dequed_data=temp.data
            self.front = self.front.next

            #if its last node
            if self.front==None:
                self.rear = None
            temp = None
            return dequed_data
        else:
            print("Queue is empty...")

    def is_empty(self):
        return self.front is None
    
    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

def reverse_queue(q1):
    st1= stack()
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))
    st1.print()

q=LQueue()
q.enqueue(Node(12))
q.enqueue(Node(13))
q.enqueue(Node(23))
q.enqueue(Node(34))
q.enqueue(Node(32))
q.enqueue(Node(42))

q.print()
reverse_queue(q)
