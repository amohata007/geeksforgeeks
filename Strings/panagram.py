def pan(a):
    s = "abcdefghijklmnopqrstuvwxyz "
    a = a.lower()
    for i in a:
        if i not in s:
            return "Not panagram"
    return "Panagram"

a = input("Enter string:")
print(pan(a))

