# #队列
# """
# 只能从队尾进入，从队首输出的环形列表
# """
# class Queue:
#     def __init__(self,size):
#         self.queue=[0 for _ in range(size)]
#         self.size=size
#         self.front=0
#         self.rear=0

#     def push(self,num):
#         if not self.is_filled():
#             self.rear=(self.rear+1)%self.size
#             self.queue[self.rear]=num
#         else:
#             raise IndexError('列表已满')

#     def pop(self):
#         if not self.is_empty():
#             self.front=(self.front+1)%self.size
#         else:
#             raise IndexError('列表为空')
            
#     def is_empty(self):
#         return self.front==self.rear
    
#     def is_filled(self):
#         return (self.rear+1)%self.size==self.front
    
    
# queue1=Queue(12)
# for i in range(11):
#     queue1.push(i)
# queue1.push(20)

# queue2=Queue(12)
# queue2.pop()

# # 队列的内置模块
# from collections import deque
# dq1=deque([1,2,3,4,5],5)
# dq1.append(6)
# dq1.popleft()
# print(dq1)

#使用队列提取文档后n行
from collections import deque
def txt_rear(filename,n):
    with open (filename,'r',encoding='utf-8') as f:
        dq=deque([],n)
        for lines in f.readlines():
            dq.append(lines)
    for i in dq:
        print(i)

txt_rear("D:\Python_files\diary.txt",5)
