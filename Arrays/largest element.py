n = int(input("Enter length of array:"))
A = []

for i in range(n):
    ele = int(input())
    A.append(ele)
mx = A[0]
# for i in range(n):
#     if mx<A[i]:
#         mx=A[i]
# print(mx)

print(max(A))