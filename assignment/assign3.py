class Node:
    def __init__(self, id, name, prio):
        self.id = id
        self.name = name    
        self.prio = prio 
        self.next = None     

# priority queue implementation using SLL
class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    # inserting a new process according to its priority
    def add_Process(self, id, name, prio):
        newNode = Node(id, name, prio)
        # if queue is empty, insert the first process
        if self.front is None:
            self.front = newNode
            print("Inserted Process")
            return

        # if new process has higher priority than front
        if newNode.prio < self.front.prio:
            newNode.next = self.front
            self.front = newNode
            print("Inserted Process")
            return

        temp = self.front
        prev = None
        # traverse while existing priority is less than or equal to the new process priority
        while temp and temp.prio <= newNode.prio:
            prev = temp
            temp = temp.next
        # insert the new node at the correct position 
        newNode.next = temp
        prev.next = newNode
        print("Inserted Process")

    # displays all processes in the priority queue
    def display_all(self):
        # check if queue is empty
        if self.front is None:
            print("Queue underflow!")
            return
        temp = self.front
        # traverse and display every process
        while temp:
            print(f"Process ID: {temp.id}, Name: {temp.name} & Priority : {temp.prio}")
            temp = temp.next
        print("--------------------")

    # removes and executes the highest-priority process
    def dequeue(self):
        # check if queue is empty
        if self.front is None:
            print("Queue underflow!")
            return
        temp = self.front
        self.front = temp.next
        print(f"Executed Process : {temp.name}!")
        temp = None

    # displays the process that will execute next
    def display_next(self):
        # check if queue is empty
        if self.front is None or self.front.next is None:
            print("Theres no next process!")
            return
        # display the front process
        temp = self.front
        print(f"Next Process : Process ID: {temp.id}, Name: {temp.name} & Priority : {temp.prio}")

    # counts the total number of processes in the queue
    def count(self):
        # if queue is empty count is zero
        if self.front is None:
            print(f"Processes count : {0}")
            return

        count = 0
        temp = self.front
        # traverse the linked list and increment count
        while temp:
            count += 1
            temp = temp.next
        print(f"Processes count : {count}")

p = PriorityQueue()
p.add_Process(1, "p1", 4)
p.add_Process(2, "p2", 2)
p.add_Process(3, "p3", 1)
p.add_Process(4, "p4", 3)
p.add_Process(5, "p4", 1)
p.display_all()
p.dequeue()
p.display_all()
p.display_next()
p.count()
