n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)
print(A)
# print(A[::-1])

#using builtin function
A.reverse()
print(A)