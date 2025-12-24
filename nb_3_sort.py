# # quick_sort
# def partition(lst,left,right):
#     insert_value=lst[left]
#     while left<right:
            
#         while lst[right]>=insert_value and right>left:
#             right-=1
#         lst[left]=lst[right]

#         while lst[left]<=insert_value and right>left:
#             left+=1
#         lst[right]=lst[left]
    
#     lst[left]=insert_value
#     return left

# def quick_sort(lst,left,right):
#     if left<right:     
#         mid=partition(lst,left,right)
#         quick_sort(lst,left,mid)
#         quick_sort(lst,mid+1,right)
#     return list1

# list1=[9,4,1,3,0,6,8,2,3]
# print(quick_sort(list1,0,len(list1)-1))


#堆排序heapq实现topk问题
   

# 归并排序
def merge(lst,left,mid,right):

    i,j=left,mid+1
    new_lst=[]

    while i<=mid and j<=right:
        if lst[i]<lst[j]:
            new_lst.append(lst[i])
            i+=1
        else:
            new_lst.append(lst[j])
            j+=1
    while i<=mid:
        new_lst.append(lst[i])
        i+=1
    while j<=right:
        new_lst.append(lst[j])
        j+=1

    lst[left:right+1]=new_lst


def merge_sort(lst,left,right):
    if left<right:
        mid=(left+right)//2
        merge_sort(lst,left,mid)
        merge_sort(lst,mid+1,right)
        merge(lst,left,mid,right)

# test=[1,3,5,7,2,4,6,8]
# merge(test,0,4,7)


test_list=[3,1,7,3,8,0,6,9,4]
merge_sort(test_list,0,8)
print(test_list)
    




