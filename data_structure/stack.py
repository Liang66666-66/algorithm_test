#栈
"""
只能从队尾进入或输出的列表
"""
def kuohaomatch(my_str):
    """
    使用栈解决括号字符串匹配问题
    """
    stk=[]
    my_dict={'{':'}','[':']','(':')'}
    for i in my_str:
        if i in {'{','[','('}:
            stk.append(i)
        else:
            if len(stk)>0:
                if i==my_dict.get(stk[-1]):
                    stk.pop()
                else:
                    return False
            else:
                return False
            
    if len(stk)==0:
        return True
    else:
        return False

the_str='{[(){}]}'
false_str='{[}]'
o_false_str='{'
o1_false_str=']['

print(kuohaomatch(the_str))
print(kuohaomatch(false_str))
print(kuohaomatch(o_false_str))
print(kuohaomatch(o1_false_str))



        

