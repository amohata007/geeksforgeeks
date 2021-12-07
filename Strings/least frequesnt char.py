from collections import Counter
a = input("Enter string:")
x = dict(Counter(a))
print(min(x,key=x.get))  #term to remember


#for max
print(max(x,key=x.get))