a = input("Enter string:")
l = len(a)
if l%2==0:
    if a[:l//2]==a[l//2:]:
        print("Symmetrical")
    else:
        print("Not Symmetrical")
else:
    if a[:l//2]==a[l//2 + 1:]:
        print("Symmetrical")
    else:
        print("Not Symmetrical")

if a==a[::-1]:
    print("Palindromic")
else:
    print("Not Palindromic")