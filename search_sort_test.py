# #1.判断两个单词包含的字母是否一致
# word1='banana'
# word2='nabaanm'

# def word_check(a,b):

#     lst1=list(a)
#     lst2=list(b)
#     for val in lst1:
#         for i,val2 in enumerate(lst2):
#             if val2==val:
#                 lst2.pop(i)
#                 break
#         else:
#             return False
        
#     if lst2==[]:
#         return True
#     else:
#         return False  

# print(word_check(word1,word2))

# #二维数组查找
# def narry_search(lst,num):
#     left=0
#     right=len(lst)-1
    
#     while left<=right:
#         mid=(left+right)//2
#         if lst[mid][0]>num:
#             right=mid-1
#         elif lst[mid][-1]<num:
#             left=mid+1
#         else:
#             left_i=0
#             right_i=len(lst[mid])-1
#             while left_i<=right_i:
#                 mid_i=(left_i+right_i)//2
#                 if lst[mid][mid_i]<num:
#                     left_i=mid_i+1
#                 if lst[mid][mid_i]>num:
#                     right_i=mid_i-1
#                 else:
#                     return True
#             else:
#                 return False
#     else:
#         return False


# my_lst=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[16,19,23,99]]
# the_num=19
# print(narry_search(my_lst,the_num))

# #下标求和
# def add(lst,num):
#     i=0
    
#     while i<=len(lst)-1:
#         j=i+1
#         while j<=len(lst)-1:
#             if lst[i]+lst[j]!=num:
#                 j+=1
#             else:
#                 return (i,j)
#         else:
#             i+=1
#     else:
#         return None
    
# print(add([1,2,3,4,7],8))
 



