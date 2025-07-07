# List is datatype where you can store multiple item under 1 name.MOre technically,list acts like dynamic arrays which you can add more items on fly

# Array Vs List
# 1)arrayas are fixed size List are dynamic
# 2)Arrays are Homogenous List are Heterrogenous
# 3)Array having more speed of execution and takes less memory as compared to list

# not necessary  to store items of List in homogenoues location
L=[1,2,3,4]
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))

# Characteristic of list
# 1)Ordered
# 2)Changeble/Mutable
# 3)Heterogeous
# 4)Dynamic
# 5)Can be Nested
# 6)can contains any kind of object

# ______________________________________________________________________

# Creating List
# Empty
print([])
# 1D
print([1,2,3,4])
# 2D
print([1,2,3,[4,5]])
# Heterogenou list
print(1,True,3.5)
# Using Type Conversion
print(list("Hello"))

# ______________________________________________________________________

# Accessing Items from List
# Indexing on 1D 
L=[1,2,3,4]
# Positive Indexing
print(L[2])
# Negative Indexing
print(L[-1])

# Indexing on 2D 
L=[1,2,3,[4,5]]
print(L[-1][-2])
print(L[3][0])

# Slicing
print(L[:])
print(L[::-1])
print(L[:3:2])

# ______________________________________________________________________

# Adding Item
# 1)append==>Adding Only One item
L=[1,2,3,4,5]
L.append(6)
print(L)

# 2)extend==>Adding multiple item
# If we pass string like 'Delhi' in extend then python will add like single character in list
L.extend([7,8,9])
print(L)

# 3)insert==>Adding to desired index
L.insert(1,100)
print(L)

#  ______________________________________________________________________

# Editing items in List
L=[1,2,3,4]
L[-1]=5
print(L)

# Editing with Slicing
L[:]=[1,2,3,3]
print(L)

#  ______________________________________________________________________

# Deleting Items from List
# 1)del
# del(L)
# deletion using indexing
del(L[-1])
# deletion using slicing
del(L[1:3])

# 2)remove(number)
L=[1,2,3,4,5]
L.remove(5)

# 3)pop(index)
L.pop(1)
print(L)

# 4)clear==>empty list
L.clear()
print(L)

#  ______________________________________________________________________

# Operation on List
# 1)Arithematic Operator
l1=[1,2]
l2=[3,4]
# concatenation
print(l1+l2)

# Multiplaction
print(l1*4)

# 2)Membership Operator
