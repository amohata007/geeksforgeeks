n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)
m = int(input("Search for element:"))
if m in A:
    print("Exist")
else:
    print("Not exist")

#can also use count 