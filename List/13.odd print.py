n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)

print(list(filter(lambda x:x%2!=0,A)))

