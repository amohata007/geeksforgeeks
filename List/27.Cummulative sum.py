n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)

for i in range(n-1):
    A[i+1] += A[i]

print(A)