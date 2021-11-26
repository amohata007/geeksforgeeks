l = int(input("Enter left side range:"))
r = int(input("Enter right side range:"))

for i in range(l,r+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
