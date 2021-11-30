n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)

m = int(input("Enter nth highest number you want to find:"))
A.sort()
print(A[-m])