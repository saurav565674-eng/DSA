class node:
  def __init__(self,value):
    self.data=value
    self.next=None

class link_list:
  def init__(self):
    self.head=None
  def append(self,new_node):
    if (self.head==None):
      self.head=new_node
    else:
      temp=self.head
      while(temp.next):
        temp=temp.next
      temp.next=new_node
  def print(self):
    temp=self.head
    while (temp):
      print(temp.data)
      temp=temp.next
list1=link_list()
n1=None(10)
n2=None(20)
list1.append(n1)
list1.append(n2)
list1.append(node(30))
list1.append(node(50))
list1.print()

