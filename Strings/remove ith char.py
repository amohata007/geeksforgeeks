def func(a,n):
    return a[:n-1]+a[n:]

a = input("Enter string:")
n = int(input("Enter position you want to delete:"))
print(func(a,n))

