n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)
cnt=0
for i in A:
    s = 0
    while(i!=0):
        rem = i%10
        s+=rem
        i //= 10
    A[cnt]=s
    cnt+=1
print(A)

# # Python3 code to demonstrate
# # Sum of number digits in a List
# # using sum() + reduce()
# from functools import reduce
#
# # Initializing list
# test_list = [12, 67, 98, 34]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# # Sum of number digits in List
# # using sum() + reduce()
# res = [reduce(lambda x, y: int(x) + int(y), list(str(i))) for i in test_list]
#
# # printing result
# print("List Integer Summation : " + str(res))