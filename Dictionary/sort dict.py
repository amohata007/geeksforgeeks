d = {'one':1,'three':3,'five':5,'two':2,'four':4}
print(dict(sorted(d.items())))  #key as base

#sort by value
print(sorted(d.items(),key=lambda v:v[1],reverse=True))
print(sorted(d.items(),key=lambda v:v[1])) #v[0] indicates keys whereas v[1] indicates values


#METHOD 2       using Itemgetter is more optimal

# Python code demonstrate the working of sorted()
# and itemgetter

# importing "operator" for implementing itemgetter
# from operator import itemgetter
#
# # Initializing list of dictionaries
# lis = [{"name": "Nandini", "age": 20},
#        {"name": "Manjeet", "age": 20},
#        {"name": "Nikhil", "age": 19}]
#
# # using sorted and itemgetter to print list sorted by age
# print
# "The list printed sorting by age: "
# print
# sorted(lis, key=itemgetter('age'))
#
# print("\r")
#
# # using sorted and itemgetter to print list sorted by both age and name
# # notice that "Manjeet" now comes before "Nandini"
# print
# "The list printed sorting by age and name: "
# print
# sorted(lis, key=itemgetter('age', 'name'))
#
# print("\r")
#
# # using sorted and itemgetter to print list sorted by age in descending order
# print
# "The list printed sorting by age in descending order: "
# print
# sorted(lis, key=itemgetter('age'), reverse=True)

