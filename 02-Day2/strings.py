# string are sequence of Unicode Character

# Creating String
# There are many cases where we need inverted symbol so there are more than one inverted commas is used to represent string
s="hello"
s='hello'
# for multiline string
s='''hello'''
s="""hello"""
# another way to create a string is by using str function
s=str('hello')

# ________________________________________________________________________

# Indexing in String
s="Hello World"

# positive indexing==>starting from zero and moving toward right
print(s[2])
print(s[5])  #count space also
# print(s[11])  #inex 11 is not exist there it throw an error as index out of bound

# Negative Indexing==>starting from -1 and moving toward left
print(s[-1])  #fetching last character

# ________________________________________________________________________

#Slicing 
# Syntax==>string[start:end:stepsize]
s="Hello World"

# positive slicing
print(s[2:3])
print(s[:])  #print whole String
print(s[0:6:2])

# Negative slicing===>start index is always greater here
print(s[-5:])
print(s[6:0:-1])
print(s[::-1])  #reverse the string

# ________________________________________________________________________

# Editing in Strings
s="Hello World"
# s[0]='h'    ==>We cannot change string once it created thats why string is immuatable

# Delete the String
# we cannot delete partial string
del(s)

# ________________________________________________________________________

# Operation on String

# 1) Arithematic operation
#  + Operator==Concatenation 
print("John"+"Smith")

# * Operator
print("*"*50)

# 2)Relational Operator
print('delhi'=='Delhi')
print("Mumbai">"pune") #check on ascii value(lexographically)
# when there is any value in string it treated as 1 or True and string is empty it treated as false or 0
print("hello"and"world")
print("hello"or"world")
print(""and"world")
print(""or"world")


# 3)Looping in String
for i in "John":
    print(i)

for i in "delhi":
    print("pune")

# 4)membership Operator
print("D" in 'Delhi')

# ________________________________________________________________________

# Common Function in String
# 1)len function
print(len("hello"))

# 2)print  character which having minimun ascii value
print(min("halks jksjd"))

# 3)Sorted==>sort Asending on ascii value
print(sorted("hello"))
# sort descending
print(sorted("hello",reverse=True))

# 4)Capitalize===>Capitalize first World Only
s="soman kunal"
print(s.capitalize())

# 5)title()===>Capitalize first letter of every word
print(s.title())

# 6)upper()==>convert to upper case
print(s.upper())

# 7)upper()==>convert to upper case
print(s.lower())

# 8)swapcase()==>lower to upper and vise versa
print(s.swapcase())

# 9)count==>count occurance
'soman kapoor'.count('a')

# 10)find=>find index of item if it never exist then it return -1 but it cannot throw an error
print("shrdhha".find("s"))

# 11)index===>it charater not exist then it throws an error
# print("shrdhha".index("y"))

# 12)endswith
print("anil".endswith("l"))

# 12)startswith
print("anil".startswith("l"))

# 13)format
name="amol"
gender="male"
print("my name is {} and gender is  {}".format(name,gender))
# fomatting by order
print("my name is {1} and gender is{0}".format(gender,name))


# 14)isalnum==>only aplhabet and character symbols not allowed
print("ankita".isalnum())

# 15)isalpha==>only aplhabet
print("anki".isalpha())

# 16)isalpha==>only digit
print("anki".isdigit())

# 17)isIdentifier==>checking for valid indentifire
print("ankita".isidentifier())

# 18) split
print("my name is Kunal".split())
# splitting by any character
print("my name is Kunal".split("m"))

# 19)join
print(" ".join(['my', 'name', 'is', 'Kunal']))

# 20)Replace===>if it not found return nothing
print("my name is Kunal".replace("Kunal","soham"))

# 21)strip==>romving spaces
print("my name is Kunal         ".strip())
