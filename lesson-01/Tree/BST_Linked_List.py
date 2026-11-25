class Node:
    def __init__(self,value):
        self.left=None
        self.data=value 
        self.right=None
class BST:
    cnt=0
    def __init__(self):
        self.root=None
        self.cnt=0


    
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


    def countleaf(self,rt):
        
        if rt is None:
            return
        else:
            self.countleaf(rt.left)
            if rt.left is None and rt.right is None:
                self.cnt+=1
            self.countleaf(rt.right)
            
    def countleaf_in_left(self,rt):
        if rt is None:
            return
        else:
            self.countleaf(rt.left)   
            self.cnt+=1
            self.countleaf(rt.right)  
    
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

    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right 
        return False
    
    def minimum(self,rt):
        temp =rt
        while temp.left:
            temp=temp.left
        print("\nmin",temp.data)
        temp=rt
        while temp.right:
            temp=temp.right
        print("\nmax",temp.data)


    def del_node(self,rt,val):
        if rt is None:
            return rt
        if val<rt.data:
            rt.left=self.del_node(rt.left,val)
        elif val>rt.data:
            rt.right=self.del_node(rt.right,val)
        else:
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left
        # when node has both left and right child
        succ=self.get_successor(rt)
        rt.data=succ.data
        rt.right=self.del_node(rt.right,succ.data)
        return rt

    def get_successor(self,temp):
        temp=temp.right
        while temp is not None and temp.left is not None:
            temp=temp.left
        return temp


b=BST()
b.insert(Node(23))               
b.insert(Node(223))               
b.insert(Node(234))               
b.insert(Node(13))               
b.insert(Node(123))               
b.insert(Node(66))               
b.insert(Node(11))               
b.insert(Node(22))               
b.insert(Node(33))               
b.insert(Node(523)) 
print("InOrder")  
# b.inorder(b.root)
# print("\nPreOrder")  
# b.preorder(b.root)
# print("\nPostOrder")
# b.postorder(b.root) 
         
# b.minimum(b.root)

# b.del_node(b.root,123)
b.countleaf(b.root)
print("count leaf",b.cnt)# b.inorder(b.root)
b.countleaf_in_left(b.root)
print("count left lesf",b.cnt)
# if b.search(13):
#     print("\nfound")
#     b.inorder(b.root)
# else:
#     print("\nnot found")
