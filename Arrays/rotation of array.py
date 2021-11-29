n = int(input("Enter length of array:"))
A = []
for i in range(n):
    ele = int(input())
    A.append(ele)
k = int(input("Enter number of rotation:"))
print("Before rotation:")
for i in A:
    print(i,end=" ")
print()
print("After rotation:")
#left rotation
print(A[k:]+A[:k])

#right rotation
print(A[n-k:]+A[:n-k])