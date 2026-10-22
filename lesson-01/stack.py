class Node:
  def __init__(self,value):
    self.data=value
    self.next=None

class stack:
  def __init__(self):
    self.top=None

  def isempty(self):
    return self.top is None
  
  def push(self,new_node):
    new_node.next=self.top
    self.top = new_node

  def pop(self):
    if self.isempty():
      print("stack is empty ")
    else:
      temp=self.top 
      print("poped element :",temp.data)
      self.top=self.top.next
      temp=None

  def reverse_stack(self):
    stk = stack()
    temp=self.top
    while temp:
      stk.push(Node(temp.data))
      temp=temp.next
    return stk

  def print(self):
    temp=self.top
    print ("stack data  ")
    while temp :
      print(temp.data)
      temp=temp.next

st = stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.print()

# st.pop()
# st.print()
s2 = st.reverse_stack()
s2.print()