a = input("Enter string:")
b = input("Enter substring:")
l = len(a)//len(b)
for i in range(l):
    if b in a:
        a = a.replace(b,'')
    else:
        continue
if a=="":
    print("YES")
else:
    print("NO")