a1 = input("String1:").split()
a2 = input("String2:").split()
x = []
for i in a1:
    if i not in a2:
        x.append(i)
for i in a2:
    if i not in a1:
        x.append(i)
print(x)

#function
# k=set(a).symmetric_difference(set(b))