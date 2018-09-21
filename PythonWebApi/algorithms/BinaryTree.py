class BinaryTree:
    class Node:

        def __init__(self, data):
            self.data=data
            self.parent=None
            self.left=None
            self.right=None

    def __init__(self):
        self.root=None

    def inorder_tree_walk(self, x):
        if x!=None:
            self.inorder_tree_walk(x.left)
            print(x.data)
            self.inorder_tree_walk(x.right)

    def tree_search(self,x,k):
        if x==None or k==x.data:
            return x
        if k<x.data:
            return tree_search(x.left,k)
        else:
            return tree_search(x.right,k)

    def iterative_tree_search(self,x,k)
        while x!=None and k!=x.data:
            if k<x.data:
                x=x.left
            else:
                x=x.right
        return x

    def tree_mininum(self,x):
        while x.left!=None:
            x=x.left
        return x
    def tree_maximum(self,x):
        while x.right!=None:
            x=x.right
        return x
    def tree_successor(self,x):
        if x.right!=None:
            return tree_minimum(x.right)
        y=x.parent():
        while x==y.right and y!=None:
            x=y
            y=x.parent()
        return y
    def insert(self,z):
        y=None
        x=self.root()

        while x!=None:
            y=x

            if z.data<x.data:
                x=x.left
            else:
                x=x.right

        z.parent=y

        if y==None:
            self.root=z
        elif z.data<y.data:
            y.left=z
        else:
            y.right=z

    def transplant(self, u, v):
        if u.p==None:
            self.root=v
        elif u=u.parent.left:
            u.parent.left=v
        else:
            u.parent.right=v
        if v!=None:
            v.parent=u.parent

    def delete(self, z):
        if z.left==None:
            self.transplant(z,z.right)
        elif z.right==None:
            self.transplant(z,z.left)
        else:
            y=self.tree_mininum(z)
            if y.parent!=z:
                self.transplant(y,y.right)
                y.right=z.right
                y.right.parent=y
            self.transplant(z,y)
            y.left=z.left
            y.left.parent=y

