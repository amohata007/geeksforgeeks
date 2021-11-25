n = int(input("Enter any number for which you want to check the armstrong:"))
k=n
m = str(n)
l = len(m)
summ = 0
# for i in m:
#     summ += int(i)**l

#using while
while(n!=0):
    rem = n%10
    summ += rem**l
    n //= 10

print("YES" if summ==k else "NO")

