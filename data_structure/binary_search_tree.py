class bitreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.parent=None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root=None
        pass

    def insert_node(self,node):
        cur_root=self.root

        if not cur_root:
            self.root=node
        while cur_root:
            if node.data<cur_root.data:
                if cur_root.lchild:
                    cur_root=cur_root.lchild
                else:
                    cur_root.lchild=node
                    node.parent=cur_root

            elif node.data>cur_root.data:
                if cur_root.rchild:
                    cur_root=cur_root.rchild
                else:
                    cur_root.rchild=node
                    node.parent=cur_root
            else:
                return
            
    #前序遍历二叉树
    def pre_order(self,rootnode):
        if rootnode:
            print(rootnode,end=' ')
            self.pre_order(rootnode.lchild)
            self.pre_order(rootnode.rchild)

    #中序遍历二叉树
    def in_order(self,rootnode):
        if rootnode:
            self.in_order(rootnode.lchild)
            print(rootnode,end=' ')
            self.in_order(rootnode.rchild)

    #后序遍历二叉树
    def post_order(self,rootnode):
        if rootnode:
            self.post_order(rootnode.lchild)
            self.post_order(rootnode.rchild)
            print(rootnode,end=' ')

tree1=BinarySearchTree()

for i in [2,5,6,9,1,4,7,3,8]:

    tree1.insert_node(bitreeNode(i))

tree1.pre_order(tree1.root)
print()
tree1.in_order(tree1.root)
print()
tree1.post_order(tree1.root)



