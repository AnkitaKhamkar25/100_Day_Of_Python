
RESET   = "\033[0m"
GREEN   = "\033[1;32m"
RED     = "\033[1;31m"
YELLOW  = "\033[1;33m"
CYAN    = "\033[1;36m"
MAGENTA = "\033[1;35m"

print()
print(CYAN + "Welcome to the Menu-Driven Calculator\n" + RESET)


print(YELLOW + "Select operation:" + RESET)
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division\n")

choice = input(" Enter your choice (1/2/3/4): ")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if choice == '1':
    result = num1 + num2
    print(GREEN + f"Result: {num1} + {num2} = {result}" + RESET)

elif choice == '2':
    result = num1 - num2
    print(GREEN + f"Result: {num1} - {num2} = {result}" + RESET)

elif choice == '3':
    result = num1 * num2
    print(GREEN + f"Result: {num1} x {num2} = {result}" + RESET)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(GREEN + f"Result: {num1} ÷ {num2} = {result}" + RESET)
    else:
        print(RED + "Error: Cannot divide by zero!" + RESET)

else:
    print(RED + "Invalid choice. Please enter 1, 2, 3, or 4." + RESET)
