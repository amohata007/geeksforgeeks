# n = int(input("Enter number of elements:"))
# ele = input("Space seperated input")
# ls = ele.split()
# print(ls)

n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)
# A[0],A[n-1]=A[n-1],A[0]
# print(A)

start,*middle,endd = A            #Important
A = [endd,*middle,start]
print(A)