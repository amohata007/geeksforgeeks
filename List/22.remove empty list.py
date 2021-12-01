lst = [2,3,5,[],3,5,[]]
# for i in lst:
#     if i==[]:
#         lst.remove(i)
# print(lst)

#using filter
x = list(filter(None,lst))
print(x)



# x = list(filter(lambda x:x!=5,lst))
# print(x)