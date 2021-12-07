# from collections import Counter
# a = input("Enter string:")
# x = Counter(a.split())
# print(dict(x))
#
# #converting dict to list of tuples
# ls = list(x.items())
# print(ls)


#without using counter
a = input("Enter string:")
res = {key: a.count(key) for key in a.split()}
print(res)