class Node:

    def __init__(self,data):
        self.data=data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None


    def isEmpty(self):
        if self.top == None:
            return True


    def push(self,data):
        newNode = Node(data)
        if self.top == None:
            self.top = newNode
            return 

        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.isEmpty():
            print("Stack underflow!")
            return

        t = self.top

        pop_data = t.data
        self.top = self.top.next
        t.next = None
        t= None

        return pop_data

    
    def display(self):
        if self.isEmpty():
            print("Stack underflow!")
            return 

        t = self.top
        print("Stack elements: ")
        while t:
            print(t.data,end=" ")
            t=t.next
        print()

    def reverseString(self,string):
        temp = Stack()

        for x in string:
            temp.push(x)

        print("Reverse: ",end="")
        while not temp.isEmpty():
            print(temp.pop(),end="")

        print()

    def reverseStack(self):
        reverseStack = Stack()
        t = self.top
        while t:
            reverseStack.push(t.data)
            t=t.next

        print("Stack elements in reverse order: ")
        reverseStack.display()


stack = Stack()
stack.push(2)
stack.push(4)
stack.push(6)
stack.display()
stack.reverseString("assinment")
stack.reverseStack()