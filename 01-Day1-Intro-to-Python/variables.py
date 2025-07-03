# Rule for naming variables
# 1)Must start with letter(a-z,A-Z) or an underscore
# 2)Cannot start with a number
# Can contain letters, digits, and underscores
# Case-sensitive (Name and name are different)
# Cannot use Python keywords like if, class, for, etc.


# Example
name="john"  #string
age=25       #integer
height=9.0   #float
is_student=False #boolen

# multiple assignment
x=y=z=10
a,b,c=4,5,9

# Python is dynamically typed language that means Python variable can change there data type
x=0      #x is integer
x="john"  # now x is string


# Calculating length of variable and print it
print("lenght is : ",len(input("Enter you name: ")))


name = "Ankita"
print("\033[1;32mName:\033[0m", name)