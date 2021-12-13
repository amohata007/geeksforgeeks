#Best case - O(n)  --- In case the array is already sorted
#Average case - O(n^2)
#Worst case - O(n^2)

#Its is stable algorithm

n = int(input("Enter length of list: "))
A=[]
for i in range(n):
    ele = int(input("Enter Element:"))
    A.append(ele)
print("Before Sorting: ",A)
for j in range(n-1):
    for i in range(n-1-j):
        if A[i]>A[i+1]:
            A[i],A[i+1]=A[i+1],A[i]
            print(A)
        else:
            print(A)
    print()