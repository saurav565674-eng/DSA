class Node:

    def __init__(self,data,prio):
        self.data = data
        self.prio = prio
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None


    def append(self,data,prio):
        newNode = Node(data,prio)

        #inserting into empty queue
        if self.front == None:
            self.front = newNode
            return

        #inserting when queue isn't empty and for first position!
        t = self.front
        if t.prio > newNode.prio:
            newNode.next = t
            self.front = newNode
            return

        else:
            prev = None
            while t and newNode.prio >= t.prio:
                prev = t
                t=t.next

            prev.next = newNode
            newNode.next = t


    def print(self):
        if self.front == None:
            print("Queue Underflow")
            return

        t = self.front
        print("Queue ELements: ")
        while t:
            print(f"Data {t.data} & Prio: {t.prio}")
            t=t.next

        print("-------------------")

    def dequeue(self):
        if self.front:
            temp=self.front
            print("Node deleted:", temp.data)
            self.front=self.front.next
        else:
            print("Queue is empty.")


pQueue = PriorityQueue()




pQueue.append(22,2)
pQueue.append(1,4)
pQueue.append(44,3)
pQueue.append(6,6)
pQueue.append(55,1)

pQueue.print()
pQueue.dequeue()
pQueue.print()