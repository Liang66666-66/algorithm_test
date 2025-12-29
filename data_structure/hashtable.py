class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def add_at_tail(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            element=Node(data)
            self.tail.next=element
            self.tail=element
        return self.head,self.tail
    
    def find_data(self,target):
        key=self.head
        while key:
            if key.data==target:
                return True
            key=key.next

        else:
            return False
        
    def del_data(self,del_data):
        
        if self.head.data==del_data:
            self.head=self.head.next
            return
        
        key=self.head
        while key.next is not None:
            if key.next.data==del_data:
                behind=key.next.next
                key.next=behind
                break
            key=key.next
            
        else:
            print('未找到您要删除的节点')        
    
    def __str__(self):
        """返回链表的字符串表示，如 1->2->3->None"""
        if self.head is None:
            return "空链表"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        
        return " -> ".join(result) + " -> None"

# linklst1=LinkedList()
# linklst1.add_at_tail(1)
# linklst1.add_at_tail(2)
# linklst1.add_at_tail(3)
# linklst1.add_at_tail(4)
# linklst1.del_data(3)
# linklst1.del_data(4)
# print(linklst1)

class Hashtable:
    def __init__(self,size):
        self.size=size
        self.buckets=[LinkedList() for _ in range(size)]
        
    def hash_func(self,num):
        hash_num=num%self.size
        return hash_num
    
    def add_item(self,num):
        target_linklst=self.buckets[self.hash_func(num)]
        if not target_linklst.find_data(num):
            self.buckets[self.hash_func(num)].add_at_tail(num)
        else:
            print('重复插入了，傻逼')

    def del_item(self,num):
        target_linklst=self.buckets[self.hash_func(num)]
        target_linklst.del_data(num)
    
    def __str__(self):
        result = []
        for i, bucket in enumerate(self.buckets):
            # 如果桶不为空，显示桶索引和内容
            if str(bucket) != "空链表":  # 检查链表是否为空
                result.append(f"槽位[{i}]: {str(bucket)}")
            else:
                result.append(f"槽位[{i}]: 空")
        
        return "\n".join(result)
    
hashtable1=Hashtable(7)
hashtable1.add_item(1)
hashtable1.add_item(4)
hashtable1.add_item(8)
hashtable1.add_item(7)
hashtable1.add_item(120)
hashtable1.del_item(120)
print(hashtable1)







