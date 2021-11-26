# def fib(n):
#     c=0
#     while(n>=c):
#         a = 0
#         b = 1
#         c = a+b
#         if n == c:
#             return True
#         a = b
#         b = c
#     else:
#         return False
#
# n = int(input("Enter any number:"))
# print(fib(n))


n = int(input("Enter any number:"))
a = 0
b = 1
c = 0
if n==0 or n==1:
    print("Yes")
else:
    while(n>c):
        c = a+b
        a = b
        b = c
    if c==n:
        print("YES")
    else:
        print("NO")
