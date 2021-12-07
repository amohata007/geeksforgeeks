def spc(a):
    for i in a:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <=122:   #can also include space
            continue
        else:
            return "YES"
    return "NO"
a = input("Enter string:")
print(spc(a))

