# What is Loop?
# A loop is a programming structure that repeats a set of instructions until a condition is met.

# Why use Loops?
    #1)To avoid repeating code manually.
    #2)To make programs more efficient and dynamic.

# Where use Loop?
    # 1) Checking Items in a Shopping List
    # 2) Alarm Clock – Repeating Until You Wake Up
    # 3)Password Retry System


# __________________________________________________

# While loop

# print table 
num=int(input("Enter the number: "))
i=1
while i<11:
    print(num,"*",i,"=",num*i)
    i=i+1

# while with else
# When loop breaks it execute else statement
x=1
while x<3:
    print(x)
    x=x+1
else:
    print("limit crossed")