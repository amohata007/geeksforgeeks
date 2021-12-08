a = input("Enter string:").split()
n = int(input("Enter length:"))
for i in a:
    if len(i)>n:
        print(i)