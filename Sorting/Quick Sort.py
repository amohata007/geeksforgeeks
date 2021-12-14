#Best case - O(n(logn))
#Average case - O(n(logn))
#Worst case - O(n^2)
#divide and conquer   or partition exchange sort
# Unstable

def pivot_place(A,first,last):
    pivot = A[first]
    left = first+1
    right = last
    while True:
        while left<=right and A[left]<=pivot:
            left+=1
        while left<=right and A[right]>=pivot:
            right-=1
        if left>right:
            break
        else:
            A[left],A[right]=A[right],A[left]
    A[first], A[right] = A[right], A[first]
    return right

def quicksort(A,first,last):
    if first<last:
        p = pivot_place(A,first,last)
        quicksort(A,first,p-1)
        quicksort(A,p+1,last)



n = int(input("Enter length of list: "))
A=[]
for i in range(n):
    ele = int(input("Enter Element:"))
    A.append(ele)
print("Before Sorting: ",A)
quicksort(A,0,n-1)
print("After sorting: ",A)


