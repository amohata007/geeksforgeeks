from functools import reduce
n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)

x = reduce(lambda a,b:a*b, A)
print(x)


#using prod function
# import numpy
# n = int(input("Enter number of elements:"))
# A=[]
# for i in range(n):
#     ele = int(input())
#     A.append(ele)
# print(numpy.prod(A))   also math.prod is working fine