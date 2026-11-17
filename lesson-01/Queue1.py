class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None


    def isEmpty(self):
        if self.front == None:
            return True


    def enque(self,data):

        node = Node(data)

        if self.front ==None:
            self.front = self.rear = node
            return

        self.rear.next = node
        self.rear = node


    def deque(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        t= self.front
        self.front = self.front.next
        t= None

    def print(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        t = self.front
        print("Queue elements: ")
        while t:
            print(t.data,end=" ")
            t=t.next
        print()



q = Queue()
print(q.isEmpty())
q.enque(10)
q.enque(20)
q.enque(30)
q.print()
q.enque(40)
q.print()
q.deque()
q.print()
q.deque()
q.print()