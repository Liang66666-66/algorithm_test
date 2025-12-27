# #求阶乘
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5)) 
# print(factorial(3)) 

# #求斐波那契数列
# def fibonacci(n):
#     if n==1 or n==2:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)


# print(fibonacci(1))  # 应该输出 1
# print(fibonacci(5))  # 应该输出 5
# print(fibonacci(7))  # 应该输出 13

# #求1到n的整数之和
# def sum_numbers(n):
#     if n==1:
#         return 1
#     return n+sum_numbers(n-1)


# print(sum_numbers(5))  # 应该输出 15
# print(sum_numbers(10)) # 应该输出 55

# #递归倒序打印数字
# def print_reverse(n):
#         if n==1:
#             print(1)
#         else:
#             print(n)
#             print_reverse(n-1)
    

# print_reverse(5)

# #递归计算数字位数
# def count_digits(n):
#     if n//10<1:
#         return 1
    
#     return 1+count_digits(n//10)


# print(count_digits(12345))  # 应该输出 5
# print(count_digits(7))      # 应该输出 1
# print(count_digits(100))    # 应该输出 3

# #判断字符串是否是回文（正读反读都一样）
# def is_palindrome(s):
#     if len(s)==1:
#         return True
#     else:
#         if s[0]==s[-1]:
#             return is_palindrome(s[1:-1])
#         else:
#             return False


# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))    # False
# print(is_palindrome("a"))        # True

# #计算最大公约数
# def gcd(a, b):
#     if a==b:
#         return a
#     if a>b:
#         if a%b==0:
#             return b
#         else:
#             c=a%b
#             return gcd(b,c)
#     if a<b:
#         if b%a==0:
#             return a
#         else:
#             c=b%a
#             return gcd(a,c)


# print(gcd(12, 18))  # 6
# print(gcd(17, 5))   # 1

# #递归计算列表和
# def sum_list(lst):
#     if len(lst)==0:
#         return 0
#     return lst[0]+sum_list(lst[1::])

# print(sum_list([1, 2, 3, 4]))  # 10
# print(sum_list([5]))           # 5
# print(sum_list([]))            # 0

# #查找列表最大值
# def find_max(lst):
#     if len(lst)==0:
#         return False
#     if len(lst)==1:
#         return lst[0]
#     fir=lst.pop(0)
#     for i in lst:
#         if i >=fir:
#             return find_max(lst)
#         if i<fir:
#             pass
#     return fir


# print(find_max([3, 1, 4, 1, 5, 9]))  # 9
# print(find_max([-5, -1, -3]))        # -1
# print(find_max([7]))        
# print(find_max([1,2,3,7,8,9,3,9,4])) 

# #判断列表中是否有目标元素
# def contains(lst, target):
#     if len(lst)==0:
#         return False
#     else:
#         if lst[0]==target:
#             return True
#         else:
#             return contains(lst[1::],target)
    

# print(contains([1, 2, 3, 4], 3))  # True
# print(contains([1, 2, 3, 4], 5))  # False
# print(contains([], 5))            # False

#递归计算乘方
def power(base, exponent):
    if exponent==0:
        return 1
    else:
        return base*(power(base,exponent-1))

print(power(2, 3))   # 8
print(power(5, 2))   # 25
print(power(3, 0))   # 1 (任何数的0次方等于1)
print(power(7, 1))   # 7