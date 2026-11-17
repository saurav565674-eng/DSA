class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None     


# creating a Queue class
class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None      

    # check whether the queue is empty 
    def isEmpty(self):
        return self.rear == None

    # insert an element into the queue
    def enque(self, data):
        newNode = Node(data)

        # if queue is empty the front and rear point to new node
        if self.isEmpty():
            self.front = self.rear = newNode
            return

        # connect the new node at the end and update rear pointer
        self.rear.next = newNode
        self.rear = newNode  

    # delete an element from the queue
    def deque(self):

        # check whether queue is empty
        if self.isEmpty():
            print("Queue underflow!")
            return

        # store the front node temp
        temp = self.front

        # move front to the next node
        self.front = self.front.next

        # deleted the temp node
        temp.next = None
        temp = None

        # if queue becomes empty 
        if self.front == None:
            self.rear = None

    # display all queue elements
    def display(self):

        # check whether queue is empty
        if self.isEmpty():
            print("Queue is Empty!")
            return

        temp = self.front 
        print("Queue Elements: ")

        # traverse the linked list
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    # reverse the queue using a stack
    def reverse(self):
        top = -1
        stack = []   
        t = self.front

        # push all queue elements into stack
        while t:
            top += 1
            stack.append(t.data)
            t = t.next

        t = self.front

        # pop elements from stack and update queue
        while t:
            t.data = stack[top]
            top -= 1
            t = t.next

    # merge two queues into a new queue
    def mergeQueues(self, queue2):
        mergedQueue = Queue()

        t = self.front

        #insert elements of first queue
        while t:
            mergedQueue.enque(t.data)
            t = t.next

        t = queue2.front

        #insert elements of second queue
        while t:
            mergedQueue.enque(t.data)
            t = t.next

        return mergedQueue

    # check whether two queues are identical
    def areQueuesIdentical(self, queue2):
        t = self.front
        q = queue2.front

        # compare elements of both queues
        while t and q:
            if t.data != q.data:
                print("Queues are not identical!")
                return

            t = t.next
            q = q.next

        # check whether both queues have same length
        if t == None and q == None:
            print("Queues are Identical!")
        else:
            print("Queues are not identical!")



queue1 = Queue()
queue2 = Queue()
queue1.enque(40)
queue1.enque(60)
queue1.enque(10)
queue1.enque(80)
queue1.display()
queue2.enque(10)
queue2.enque(20)
queue2.enque(30)
queue2.enque(40)
queue2.display()
queue1.areQueuesIdentical(queue2)