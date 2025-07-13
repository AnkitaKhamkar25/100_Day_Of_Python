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


# Guessing Game Using while Loop
import random 
jackpot=random.randint(1,100)
guess=int(input("Enter jackpot number"))
counter=1
while guess!=jackpot:
    if guess<jackpot:
        print("guess higher")
    else:
        print("guess lower")
    guess=int(input("Enter jackpot number"))
    counter+=1

else:
    print("correct guess")
    print("attempt",counter)


# __________________________________________________

# For Loop
# syntax:for i in range(start,end,stepsize)
for i in range(1,11):
    print(i)


for i in range(1,11,2):
    print(i)  

# traversing in string using for loop:
for i in 'Delhi':
    print(i) 

# traversing on list
for i in [1,2,3,4,5]:
    print(i)

# traversing on tuple
for i in (1,2,3,4,5):
    print(i)


