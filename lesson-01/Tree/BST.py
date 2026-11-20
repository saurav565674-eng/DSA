class Node:
    def __init__(self,value):
        self.left=None
        self.data=value 
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None:          #BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return 
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return 
                    else:
                        temp=temp.right   


    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end =" ")
            self.inorder(rt.right) 
  
    
    def preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.data,end =" ")
            self.preorder(rt.left)
            self.preorder(rt.right) 


    def postorder(self,rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right) 
            print(rt.data,end =" ")
    def minimum(self,rt):
        temp =rt
        while temp.left:
            temp=temp.left
        print("\nmin",temp.data)
        temp=rt
        while temp.right:
            temp=temp.right
        print("\nmax",temp.data)
b=BST()
b.insert(Node(23))               
b.insert(Node(223))               
b.insert(Node(234))               
b.insert(Node(13))               
b.insert(Node(123))               
b.insert(Node(523)) 
print("InOrder")  
b.inorder(b.root)
print("\nPreOrder")  
b.preorder(b.root)
print("\nPostOrder")
b.postorder(b.root) 
         
b.minimum(b.root)