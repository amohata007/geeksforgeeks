a = input("Enter string:")
b = input("Enter substring:")
la = len(a)
lb = len(b)
cnt = 0
for i in range(la-lb+1):
    if a[i:i+lb] == b:
        cnt+=1
print(cnt)