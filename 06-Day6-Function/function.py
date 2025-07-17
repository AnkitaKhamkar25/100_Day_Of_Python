#  What is a Function?
# A function in Python is a reusable block of code that performs a specific task.
# It helps to:
    # Organize code into smaller, manageable pieces.
    # Avoid code repetition.
    # Make code reusable and readable.

# priciple of function:
    # abstraction
    # decomposition

#syntax of function:
# def name_of_function() :
        # """docstring==>used to provide information about function"""
        # function body
        # return
# calling the function
# name_of_function()


# sample function
def is_even(num):
    """This function return if a given number is odd or even
    input-any valid integer
    output-16th nov 2022
    """
    if num%2==0:
        return "even"
    else:
        return "odd"
    
for i in range(1,100):
    x=is_even(i)
    print(i,"is",x)


# accessing the documentation
print(is_even.__doc__)



# __________________________________________________

# parameter vs argument
# def is_even(num):  #here num is parameter
# x=is_even(i):here  num is argument

# __________________________________________________

# Types of Argument

# 1)default Argument
# when argumenet is not given then default argument is used
def power(a=1,b=1):
    return a**b

power(2,5)

# 2)positinal argument

# 3)keyword argument
# passing argument with name
power(b=9,a=7)

# __________________________________________________

# *args and kwargs*
# This  are special type of python function that are used to pass variable length of argument the function

# 1)args==>allow to pass variable number of non-keyword argument to function
# not necesaary to used args word only it can work with any name
def multi(*args):
    product=1
    for i in args:
        product=product*i
    
    print(args) #stores value in tuple
    return product

multi(1,2,3,4,5)


# 2)kwargs==>allow to pass variable number of keyword argument to function
# they contains key valua pair like python dictionary
def display(**kwargs):
    for(key,value) in kwargs.items():
        print(key,'->',value)
display(India="delhi",Nepal="kathmandu")

# order of argument matters:normal->args->kwargs


# __________________________________________________

# function without return
def even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
even(20) # this return even        
print(even(20))    #this return none that return by function


# __________________________________________________

# Scope of variable
# local variable:variable that comes under function scope
                # main cannot use local variable 
# global variable:variable that comes under main program
                # local can use global variable 

# global variable and local variable can have same names

# __________________________________________________

# Nested Function
# function within function
def f():
    def g():
        print("inside function g")
    g()
    print("inside function f")

f()

# we cannot call function which nested within another function 
# def f():
#     def g():
#         print("inside function g")
#     g()
#     print("inside function f")

# g()

# __________________________________________________

# function is first call citizen
# It means it can perform all operation that datatype can perform

# type and id
def square(num):
    return num**2
type(square)
id(square)

# reassign==>we can assign function to the variable
x=square


# deleting function
# del square

# storing
L=[1,2,3,square]
L[-1](3)

# function is immutable datatype

# returnig a function
def f():
    def x(a,b):
        return a+b
    return x
val=f()(3,4)
print(val)


# _______________________________

# Lambda function
# it is small anoymous function which does not have any name
# syntax= lambda a,b:a+b
# has no return value
# not reusable
# it used with higher order function

a=lambda x:x**2
print(a(4))


# _______________________________

# map function
map(lambda x:x**2,[1,2,3,4,5])