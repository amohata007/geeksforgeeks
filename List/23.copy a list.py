#problem with this technique is that modifying a will also modify b
a=[1,2,3,4,5]
b = a
b.append(6)
print(a)
print(b)

#so list slicing
a=[1,2,3,4,5]
b = a[:]
b.append(6)
print(a)
print(b)


# Python code to clone or copy a list
# Using the in-built function extend()
# def Cloning(li1):
#     li_copy = []
#     li_copy.extend(li1)
#     return li_copy
#
#
# # Driver Code
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# print("Original List:", li1)
# print("After Cloning:", li2)


# Python code to clone or copy a list
# Using bilt-in method copy()
def Cloning(li1):
    li_copy = []
    li_copy = li1.copy()
    return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)