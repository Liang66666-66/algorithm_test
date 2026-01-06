#创建节点类
class Node:
    def __init__(self,item):
        self.item=item #节点本身
        self.next=None #节点连接的节点

# 创建链表(头部更新)
def create_head_linklist(lst):
    head=Node(lst[0])#链表头指针

    #从第二个元素开始遍历
    for i in lst[1:]:
        element=Node(i) #创建节点
        element.next=head #节点连接到头节点前
        head=element #更新头节点

    key=head
    while key:
        print(key.item,end=' ')
        key=key.next
    
    return head

# 创建链表(尾部更新)     
def create_tail_linklist(lst):
    head=Node(lst[0]) #确定链表头指针
    tail=head #链表尾指针等于链表头指针

    #从第二个元素开始遍历
    for i in lst[1:]:
        element=Node(i) #创建节点
        tail.next=element #节点连接到尾节点后
        tail=element #链表尾节点更新
    
    key=head
    while key:
        print(key.item,end=' ')
        key=key.next
    
    return head


#链表新增节点
def linklist_insert(lklist,num,pos):
    """
    linklist_insert 的 Docstring
    
    :param lklist: 链表的头部节点
    :param num: 要插入节点的数值
    :param pos: 要插入节点的位置
    """
    insert_element=Node(num) #创建节点
    cut_element=lklist #循环开始前，设置要切割的节点变量，并赋值为头部节点

    #循环找到要切割的位置
    for i in range(pos-2):
        cut_element=cut_element.next #cut_element即要被切割的节点

    behind_element=cut_element.next #behind_element是被切割节点的后一个节点

    insert_element.next=behind_element #将插入节点和后节点连接
    cut_element.next=insert_element #将切割节点和插入节点连接

    # 打印新的链表
    key=lklist
    while key:
        print(key.item,end=' ')
        key=key.next

    return lklist


#链表删除节点
def linklist_delete(lklist,pos):
    """
    linklist_delete 的 Docstring
    
    :param lklist: 链表
    :param pos: 要删除节点所在位置
    """

    front_element=lklist #循环开始前定义前节点，赋值为头部节点
    for i in range(pos-2): 
        front_element=front_element.next #循环找到前节点位置
    del_element=front_element.next #找到预删除节点
    behind_element=del_element.next #找到后节点
    del_element.next=None #断开预删除节点和后节点的连接
    front_element.next=behind_element #连接前节点和后节点

    # 打印链表
    key=lklist
    while key:
        print(key.item,end=' ')
        key=key.next

    return lklist


# 测试
lk2=create_tail_linklist([1,2,3,4,5,6])
print()
lk3=linklist_insert(lk2,8,4)
print()
lk4=linklist_delete(lk3,5)






