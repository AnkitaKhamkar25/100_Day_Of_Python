# In Python, conditional statements are used to perform different actions based on different conditions. 
# The main conditional statements in Python are:
# using simple example

# __________________________________________________

# if-else statement
email=input("Enter your email: ")
password=int(input("Enter password: "))
if(email=="john@gmail.com") and (password==12345):
    #  Executes the block only if the condition is true.
    print("yess,welcome")
else:
    print("no")



# elif==>When there is multiple condition
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is 5 or less")


# nested if
x = 10
if x > 5:
    if x < 20:
        print("x is between 5 and 20")



# shortHand
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
