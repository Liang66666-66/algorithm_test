# 希尔排序

# 计数排序
def jishusort(lst):
    max_num=max(lst)
    count=[0]*(max_num+1)
    for i in lst:
        count[i]+=1
    lst.clear()
    for i,val in enumerate(count):
        for j in range(val):
            lst.append(i)
    return lst

print(jishusort([1,5,1,3,7,4,3,2,2,6]))

# 桶排序
#基数排序