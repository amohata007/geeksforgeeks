n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)

#using lambda (anonymous function)
print(list(filter(lambda x:x%2==0,A)))

#naive method
# B=[]
# for i in A:
#     if i%2==0:
#         B.append(i)
# print(B)

#list comprehension
print([x for x in A if x%2==0])