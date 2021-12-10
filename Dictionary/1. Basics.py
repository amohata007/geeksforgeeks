d = {1:'Abhishek',2:'Abhi',3:'CSE'}

#type
print(type(d))

#print all keys
for i in d.keys():
    print(i)

#print all values
for i in d.values():
    print(i)

#to fetch particular key
print(d[1])
print(d.get(1))

#if any index is not present
# print(d[4])  #it will give error
print(d.get(4,"Not Found"))

#make dict with help of 2 lists
l1 = [1,2,3]
l2 = ['a','b','c']
x = dict(zip(l1,l2))
print(x)

#add new element
d[4] = 'Computer Science'
print(d)

#del
del d[4]
print(d)
#we can use pop as well
d.pop(3,"Not found")
print(d)  #more useful



