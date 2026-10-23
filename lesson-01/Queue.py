class node:
  def __init__(self,value):
    self.data=value
    self.next=None

class queue:
  def __init__(self):
    self.front = self.rear=None

  def equeue(self,new_node):
    if self.rear:
      self.rear.next=new_node
      self.rear=new_node
    else:
      self.front=self.rear=new_node
    self.rear.next=self.front

  def dequeue(self):
    if self.front:
      temp=self.front
      
      if self.front==self.rear:       #update for circular linked list
        self.rear=self.rear=None
        print("now queue is empty")
        
      else:
        self.front=self.front.next
        self.rear.next=self.front
      temp=None
    else:
      print("queue is empty")

  def print(self):
    temp=self.front
    print(temp.data , end="")
    temp=temp.next
    while temp!=self.front:
      print(temp.data,"->")
      temp=temp.next
      if temp == self.front:
        break
    print()

q=queue()
q.equeue(node(20))
q.equeue(node(10))
q.equeue(node(30))
q.equeue(node(50))
q.dequeue()
q.print()
q.dequeue()
q.print()
q.dequeue()
q.print()

