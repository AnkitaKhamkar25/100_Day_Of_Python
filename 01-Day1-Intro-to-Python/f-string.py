# f-strings are consise and readable way to include the value of python expression into string

# Basic syntax
name="john"
age=90
print(f"My name is {name} and my age is {age} ")

#formatting number
pi=3.14159
print(f"value of pi : {pi:.2f}")   # 2 decimal place


# padding and aligenment using f-string
name = "Ankita"
print(f"|{name:<10}|")  # Left-align
print(f"|{name:^10}|")  # Center-align
print(f"|{name:>10}|")  # Right-align