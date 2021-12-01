n = int(input("Enter number of elements:"))
A=[]
for i in range(n):
    ele = int(input())
    A.append(ele)

u = int(input("Enter upper range:"))
l = int(input("Enter lower range:"))
#list comprehension
print([x for x in A if x%2==0 and (x>l and x<u)])


#16-20 are same
#skip to 21st

#21
# if lst%2==0:
#     lst.remove(ele)