
def list_search(lst,target):

    left=0
    right=len(lst)-1

    while left<=right:
        mid_index=(left+right)//2
        mid_value=lst[mid_index]
        if mid_value==target:
            return mid_index
        if mid_value<target:
            left=mid_index+1  
        if mid_value>target:
            right=mid_index-1
    else:
        return None
           
        

print(list_search([1,2,3,4,5,6,7,8,9,10],100))



