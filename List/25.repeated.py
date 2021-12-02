from collections import Counter
n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)

x = Counter(A)
y = [m for m in x if x[m]>1]
print(y)