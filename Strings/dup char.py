from collections import Counter
a = input("Enter string:")
y = dict(Counter(a))
B=[]
cnt=0
for i in y.values():
    if i>1:
        print(list(y.keys())[cnt],end=" ")
    cnt+=1

