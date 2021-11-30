n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)
mx = A[0]
cnt=0
l = len(A)
while(cnt<l):
    if A[cnt]>mx:
        mx = A[cnt]
    cnt+=1
print(mx)

#using function
# print(max(A))
#
# #using sort
# A.sort(reverse=True)
# print(A[0])