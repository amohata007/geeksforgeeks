n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)
mn = A[0]
cnt=0
l = len(A)
while(cnt<l):
    if A[cnt]<mn:
        mn = A[cnt]
    cnt+=1
print(mn)

#using function
print(min(A))

#using sort
A.sort()
print(A[0])