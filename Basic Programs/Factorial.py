# n = int(input("Enter any number for which you want to find the factorial:"))
# fact=1
# for i in range(1,n+1):
#     fact *= i
# print(f"Factorial of {n} is {fact}")

#Using recursion
def func(n):
    return 1 if n==0 or n==1 else n*func(n-1)  #one liner
    # if n==0 or n==1:
    #     return 1
    # else:
    #     return n*func(n-1)
n = int(input("Enter any number for which you want to find the factorial:"))
print(func(n))
