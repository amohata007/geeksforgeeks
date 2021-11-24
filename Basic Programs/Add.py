# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# print(f"Sum of {a} and {b} is {a+b}")

#Without using arithmetic operator
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
while(b!=0):
    c = a&b
    a = a^b
    b = c<<1
print(f"Sum:{a}")

#using function
# sum(a,b)