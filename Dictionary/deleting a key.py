test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

del test_dict['Mani']
print(test_dict)

#using pop
# pop() can be used to delete a key and its value inplace. Advantage over using del is that it provides the mechanism to print desired value if tried to remove a non-existing dict. pair. Second, it also returns the value of key that is being removed in addition to performing a simple delete operation.
removed_value = test_dict.pop('Arushi', 'No Key found')
print(test_dict)