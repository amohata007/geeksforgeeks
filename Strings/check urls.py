# a = input("String").split()
# B=[]
# for i in a:
#     if 'http' in i:
#         B.append(i)
# print(a)
# print(B)

arr = [6, -8, 3, -1, 4]

for i in range(len(arr)):
	arr[i] = arr[i]*arr[i]
arr.sort()
print(arr)