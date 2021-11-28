n = int(input("Enter length of array:"))
A = []
summ = 0
for i in range(n):
    ele = int(input())
    A.append(ele)
# for i in A:
#     summ += i
# print(summ)

print(sum(A))
