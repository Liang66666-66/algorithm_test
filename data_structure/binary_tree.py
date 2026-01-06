class bitreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

    def __str__(self):
        return str(self.data)

A=bitreeNode('A')
B=bitreeNode('B')
C=bitreeNode('C')
D=bitreeNode('D')
E=bitreeNode('E')
F=bitreeNode('F')
G=bitreeNode('G')

root=E
E.lchild=A
E.rchild=G
A.rchild=C
G.rchild=F
C.lchild=B
C.rchild=D

#前序遍历二叉树
def pre_order(rootnode):
    if rootnode:
        print(rootnode,end=' ')
        pre_order(rootnode.lchild)
        pre_order(rootnode.rchild)

#中序遍历二叉树
def in_order(rootnode):
    if rootnode:
        in_order(rootnode.lchild)
        print(rootnode,end=' ')
        in_order(rootnode.rchild)

#后序遍历二叉树
def post_order(rootnode):
    if rootnode:
        post_order(rootnode.lchild)
        post_order(rootnode.rchild)
        print(rootnode,end=' ')

#层次遍历二叉树
from collections import deque

def period_order(rootnode):
    dq=deque([rootnode])
    nodes=[rootnode]
    while dq:
        curnode=dq.popleft()
        if curnode.lchild is not None:
            dq.append(curnode.lchild)
            nodes.append(curnode.lchild)
        if curnode.rchild is not None:
            dq.append(curnode.rchild)          
            nodes.append(curnode.rchild)
        continue

    for i in nodes:
        print(i,end=' ')

# pre_order(E)
# print()
# in_order(E)
# print()
# post_order(E)

period_order(E)

