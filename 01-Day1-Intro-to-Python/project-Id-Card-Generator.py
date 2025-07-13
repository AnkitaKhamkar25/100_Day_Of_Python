# Student Id Card Generator

# Use Variable to store information enterd by student
name=input("Enter Your name: ")
student_id=input("Enter your student id: ")
course=input("Enter your Course name: ")
college=input("Enter your cologe name: ")
email=input("Enter Your Email: ")


# use ANSI escape sequences to add color to terminal output.
# ANSI color codes
# here \033 is escape character,1 stands for bright ,and 34,35,36,32,33 follow this color
RESET   = "\033[0m"
BLUE    = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN    = "\033[1;36m"
YELLOW  = "\033[1;33m"
GREEN   = "\033[1;32m"
BOLD    = "\033[1m"


# ID Card Design
print()
print(f"{YELLOW}{'=' * 35}")
print(f"{CYAN}{BOLD}     \U0001FAAA   STUDENT ID CARD       {RESET}")
print(f"{YELLOW}{'=' * 35}{RESET}")

print(f"{BLUE}\U0001F464 Name       : {GREEN}{name}{RESET}")
print(f"{MAGENTA}\U0001F194 Student ID : {CYAN}{student_id}{RESET}")
print(f"{YELLOW}\U0001F393 Course     : {MAGENTA}{course}{RESET}")
print(f"{CYAN}\U0001F3EB College    : {BLUE}{college}{RESET}")

print(f"{MAGENTA}\U0001F4E7 Email      : {YELLOW}{email}{RESET}")

print(f"{YELLOW}{'=' * 35}")
print(f"\U00002705 {GREEN}ID Card Generated Successfully!{RESET}")
print(f"{YELLOW}{'=' * 35}{RESET}")
print()