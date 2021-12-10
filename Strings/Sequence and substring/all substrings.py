a = input("Enter string:")
l = len(a)
B=[]
for i in range(l):
    for j in range(i+1,l+1):
        B.append(a[i:j])
print(B)
print(len(B))
print(len(set(B)))
