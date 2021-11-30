n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)

# print(sum(A))
s=0
for i in A:
   s+=i
print(s)