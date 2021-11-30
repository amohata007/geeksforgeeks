def rem(A,val):
     pdt=1
     for i in A:
         pdt *= i
     return pdt%val



n = int(input("Enter length of array:"))
A = []
for i in range(n):
    ele = int(input())
    A.append(ele)
val = int(input("Enter quotient:"))
print(rem(A,val))

