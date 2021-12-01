from collections import Counter
n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)
m = int(input("Element you want to find:"))
# cnt=0
# for i in A:
#     if m==i:
#         cnt+=1
# print(cnt)

#using function
# print(A.count(m))

#using counter
x = Counter(A)
print(x[m])