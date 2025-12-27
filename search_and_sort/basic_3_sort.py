# # bubble sort
# def bubble_sort(lst):
#     for i in range(len(lst)-1):
#         for j in range(len(lst)-1-i):
#             if lst[j+1]<lst[j]:
#                 lst[j+1],lst[j]=lst[j],lst[j+1]
#     print(lst)

# print(bubble_sort([3,1,8,4,5,0,4]))

# # choice sort
# def choice_sort(lst):
#     for i in range(0,len(lst)-1):
#         for j in range(1+i,len(lst)):
#             if lst[j]<lst[i]:
#                 lst[j],lst[i]=lst[i],lst[j]
#     print(lst)

# print(choice_sort([3,1,8,4,5,0,4]))

# insert sort
def insert_choice(lst):
    for i in range(1,len(lst)):
        j=i-1
        insert_num=lst[i]
        while insert_num<lst[j] and j>=0:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=insert_num
    print(lst)

insert_choice([3,1,8,4,5,0,4])

        




