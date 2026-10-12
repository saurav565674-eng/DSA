class Node :
    def __init_(self,values):
        self.data=values
        self.next=None
    
class linklist:
    def __init__(self):
        
        self.head=None

    def append(self,values):
        newNode = Node(values)
        if self.head==None:
            self.head=newNode
            return
        
        t= self.head
        while t.next:
            t=t.next
        t.next=newNode


    def traverse(self):
        if self.head==None:
            print("linked list is empty")
            return
        t=self.head
        while t:
            print(t.data,end=" ->")
            t=t.tnext
        print("none")

    def insert (self,posi,values):
        if self.head == None and posi != 1:
            print("linked list is empty")
            print("connot insert at given position ")
            return 
        newNode = Node (values)
        if posi ==1:
            newNode.next=self.head
            self.head =newNode
            return 

        count=1
        t=self.head
        while (count !=(posi -1)):
            if t == None:
                print("index out of bounds!")
                return 
            t=t.next
            count +=1
        newNode.next=t.next
        t.next=newNode

    def middle(self):
        total =0
        t=self.head
        while 1!=None:
            total+=1
            t=t.next

        mid = total//2
        if total %2 !=0:
            mid +=1
        count =1
        t =self.head
        while count !=mid:
            t=t.next
            count +=1
        print(f"middle value :{t.data}")

    def delete(self,posi):
        if self.head==None:
            print("linked list should not be empty")
            return
        if posi ==1:
            self.head=self.head.nextreturn
            return
        count=1
        t=self.head
        while count !=(posi -1):
            if t==None:
                print("index out of bound")
                return
            t=t.next
            count+=1
        if t.next==None:
          print("index out of bound")
          return
        t.next=t.next.next


    def reverse(self):
        if self.head==None:
            print("linked list is empty")
            return
        result=[]
        t=self.head
        while t:
            result.append(t.data)
            t=t.next

        t=self.head
        k=0
        while t:
            t.data = result[k]
            k+=1
            t=t.next

if __name__ =="__main__":
    li=linklist()
    li.append(10)
    li.append(20)
    li.append(30)
    li.traverse()
    li.insert(2,44)
    li.insert(1,100)
    li.traverse()
    li.middle()
    li.insert(7,1234)
    li.traverse()
    li.middle()
    li.delete1()
    li.traverse()
    li.reverse()
    li.traverse(y)
  




