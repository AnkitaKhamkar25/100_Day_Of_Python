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
