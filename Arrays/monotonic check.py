n = int(input("Enter length of array:"))
A = []
for i in range(n):
    ele = int(input())
    A.append(ele)

if all(A[i] >= A[i+1] for i in range(0,n-1) or A[j] <= A[j+1] for j in range(0,n-1)):
    print("True")
else:
    print("False")