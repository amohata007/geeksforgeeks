# n = int(input("enter value:"))
# d = {}
#
# for i in range(n):
#     keys = input("Enter key:") # here i have taken keys as strings
#     values =input("Enter value:")# here i have taken values as integers
#     d[keys] = values
# print(d)


test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
A=[]
# print(list(test_dict.values()))
for i in test_dict.values():
    for j in i:
        A.append(j)
print(sorted(set(A)))

#one liner 
# res = list(sorted({ele for val in test_dict.values() for ele in val}))
