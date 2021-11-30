n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)
first = int(input("Enter first position:"))
second = int(input("Enter second position:"))

A[first-1],A[second-1]=A[second-1],A[first-1]
print(A)