class Node:
  def __init__(self,value):
    self.data=value
    self.next=None

class link_list:
  def __init__(self):
    self.head=None
  def append(self,new_node):
    if self.head==None:
      self.head=new_node
    else:
      temp=self.head
      while(temp.next):
        temp=temp.next
      temp.next=new_node

  def insert (self,new_node,pos):
    if pos==1:
      new_node.next=self.head
      self.head=new_node
    else:
      p=1
      temp=self.head
      while (p!=pos-1):
        temp=temp.next
        p+=1
      new_node.next=temp.next
      temp.next=new_node

  def delete (self,value):
    temp=self.head
    if temp.data==value:
      temp=self.head
    else:
      while(temp.data!=value and temp):
        prev=temp
        temp=temp.next
        if temp==None:
          print("value is absent")
          return
    prev.next=temp.next
    temp=None

  def reverse(self):
    curr=self.head
    prev=None
    while(curr):
      nextnode=curr.next
      curr.next=prev
      prev=curr
      curr=nextnode
    self.head=prev

  def findmid_del(self):
    temp=temp1=self.head
    prev=None
    while temp1 and temp1.next:
      temp=temp.next
      temp1=temp1.next.next
    print(temp.data)
    prev.next=None
    temp=None

  def delete_e(self):
    self.head=self.head.next
    temp=self.head
    prev=None
  
    while temp and temp.next:
      prev= temp
      temp= temp.next
    prev.next=None



  def print(self):
    temp=self.head
    while (temp):
      print(temp.data)
      temp=temp.next

list1=link_list()
n1=Node(10)
n2=Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(50))
# list1.insert(Node(555),3)
# list1.print()
list1.delete(30)
list1.print()
list1.reverse()
list1.print()
# list1.findmid_del()
# list1.print()
list1.delete_e()
list1.print()