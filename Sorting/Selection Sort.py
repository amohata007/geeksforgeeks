n = int(input("Enter length of list: "))
A=[]
for i in range(n):
    ele = int(input("Enter Element:"))
    A.append(ele)
print("Before Sorting: ",A)
for i in range(n-1):
    min_ele = min(A[i:])
    min_ind = A.index(min_ele,i)
    if A[i]!=A[min_ind]:
        A[i],A[min_ind] = A[min_ind],A[i]
    print(A)

