# project name: Tip Calculator
# To build a simple Python program that:
# Calculates how much tip each person should pay
# Based on:
#       Total bill amount
#       Tip percentage (e.g., 10%, 12%, 15%)
#       Number of people splitting the bill



# ANSI color codes
RED     = "\033[1;31m"
GREEN   = "\033[1;32m"
CYAN    = "\033[1;36m"
YELLOW  = "\033[1;33m"
MAGENTA = "\033[1;35m"
RESET   = "\033[0m"

# Top Border
print(f"{CYAN}\u2554" + "\u2550" * 75 + "\u2557")

# Welcome Message with Unicode Emoji 
print("\u2551" + f" \U0001F4B0 Welcome to the Tip Calculator \U0001F4B0 ".center(75) + "\u2551")

# Middle Border
print("\u2560" + "\u2550" * 75 + "\u2563")

# Inputs
bill = float(input(f"{YELLOW}\u2551 What was the total bill? $: {RESET}"))
tip_percent = int(input(f"{YELLOW}\u2551 What percentage tip would you like to give? (10, 12, 15): {RESET}"))
people = int(input(f"{YELLOW}\u2551 How many people to split the bill \U0001F465: {RESET}"))

# Calculations
tip = bill * (tip_percent / 100)
total = bill + tip
amount_per_person = round(total / people, 2)

# Result Border
print(f"{GREEN}\u255F" + "\u2500" * 75 + "\u2562")

# Result with Unicode emojis 
result_line = f"\u2705 Each person should pay: \U0001F4B5 ${amount_per_person:.2f}"
print("\u2551" + result_line.center(75) + "\u2551")

# Bottom Border
print("\u255A" + "\u2550" * 75 + "\u255D" + RESET)
