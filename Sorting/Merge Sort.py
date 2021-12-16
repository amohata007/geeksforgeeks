

def mergesort(x,y):
    i=j=0
    len_a = len(x)
    len_b = len(y)
    c = []
    while(i<len_a and j<len_b):
        if x[i]<=y[j]:
            c.append(x[i])
            i+=1
        else:
            c.append(y[j])
            j+=1
    while i<len_a:
        c.append(x[i])
        i+=1
    while j < len_b:
        c.append(y[j])
        j += 1
    return c

def dividesort(A):
    if len(A)<=1:
        return A
    mid = len(A)//2
    left_A = A[:mid]
    right_A = A[mid:]

    left_A = dividesort(left_A)
    right_A = dividesort(right_A)

    return mergesort(left_A,right_A)


# n = int(input("Enter length of list: "))
# A=[]
# for i in range(n):
#     ele = int(input("Enter Element:"))
#     A.append(ele)
A = [5,3,8,9,1,7,8,2,3]
print("Before Sorting: ",A)
print(dividesort(A))
