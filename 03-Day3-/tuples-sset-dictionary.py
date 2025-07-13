# Tuple in python is similar to list.The Difference between thw two is that we cannot change element of tuple once it is assigned
# In short tuple is immutable list
# Characteristic:
#   1)Ordered
#   2)Unchangable
#   3)Allow duplicates

#  ______________________________________________________________________

# Creating Tuple

# empty
t1=()
# tuple with single element
t2=(1,)
#Homogenous 
t3=(1,2,3,4)
# Heterogenous
t4=("hello",1,3.4,True) 
#Tuple within Tuple
t5=(1,2,3,4,(1,2,3,4))
# Using Type Conversion
t6=tuple("hello")


# ______________________________________________________________________

# Accessing Items 
# Indexing
t=(1,2,3,4,5)
print(t[0])
print(t[:])
print(t[::-1])
print(t[::-1])
# 2D Tuple
t2=(1,2,3,4,(1,2,3,4))
print(t2[4][0])

# ______________________________________________________________________

# Editing items
# t[0]=100
# this throws an error that tuple is immutable

# Adding Item
# this throws an error that tuple is immutable


#  ______________________________________________________________________

# Deleting Items
# we can delete whole tuple but portion of tuple cannot be deleted 
del(t2)
# del(t[2])   #this throws an error

#  ______________________________________________________________________

# Operation on Tuple
# 1)Arithematic Operator
t1=(1,2)
t2=(3,4)
# concatenation
print(t1+t2)

# 2)Membership Operator
print(5 in t1)
print(2 not in t2)

# Multiplaction
print(t1*4)

#  ______________________________________________________________________

# function in Tuple
# len/min/max/sorted
t=(2,3,4,7,2)
print(len(t))  #provide length of Tuple
print(max(t))  #provide max item of Tuple
print(min(t))  #provide min item of Tuple
print(sorted(t)) #provide sorted Tuple

# count(item)
print(t.count(2))

# index==>provide index of an item
print(t.index(2))


#  ______________________________________________________________________

# Diffrence between List And Tuple
# 1)tuples are immutable and list are mutable
# 2)tuples are faster than list
# import time
# L=list(range(100000000))
# T=tuple(range(10000000))
# start=time.time()
# for i in L:
#     i*5
# print("List time",time.time()-start)

# start =time.time()
# for i in T:
#     i*5
# print("Tuple time",time.time()-start)

# 3)memory takes less tuple than list
# 4)List having more builtin function than tuple
# 5)List is more error prone than tuple



#  ______________________________________________________________________

# Special syntax
# tuple unpacking==>Both side and count of variable must be same
a,b,c=(1,2,3)
# a,b=(1,2,3)  #This throw error

# swapping using Tuple unpacking
a=1
b=2
a,b=b,a
print(a,b)

# Others in Tuple
a,b,*others=(1,2,3,4,5)
print(a,b)
print(others)


# Zipping in Tuple
a=(1,2,3,4)
b=(2,3,4,5)
list(zip(a,b))


#  ________________________________________________________________________________________________________________-

# Sets
# Characteristic:
    # ordered
    # Mutable
    # No Duplicates
    # Cant contain Mutable data type===>set cannot contain set
#  ______________________________________________________________________


# Creating Tuple

# empty
s=set()
print(s)
# 1D 
s1={1,2,3}
# 2D===>set cannot contain set
# s1={a,2,3,{5,6}}   #Throw error

# Homo and Hetro
s3={3,2.0,True,"hello",(9,3,4)}
print(s3)

# Using type Conversion
s4=set([1,2,3])
print(s4)

s1={1,2,3}
s2={2,1,3}
print(s1==s2)


#  ______________________________________________________________________


# Accessing  and editing Items
# We cannot acess items from set

# ______________________________________________________________________

# Adding Item
s={1,2,3,4}
# add===>adding single item
s.add(5)
# update==>adding multiple element
s.update([1,2,3])
print(s)

#  ______________________________________________________________________

# Deleting Items
# 1)del==>delete whole set cannot delete portion of set
# del(s)

# 2)discard==>delete one item,when item not present it  not show error
s.discard(2)
print(s)

# 3)remove==>when item not present it show error
s.remove(1)
print(s)

# 4)pop=>delete random item
s.pop()
print(s)

# 5)clear=>empty set
s.clear()

#  ______________________________________________________________________

# Operation On set
s1={1,2,3,4}
s2={4,5,6,7}
# union
print(s1|s1)
# intersection
print(s1&s1)
# Differnce
print(s1-s2)
print(s2-s1)
# Symetric Difference
print(s1^s2)

# 2)Membership Operator
print(5 in s1)
print(2 not in s2)

# 3)Loops
# for i in s1:
#     print(i,sep=" ")

#  ______________________________________________________________________

# function in set
# 1)len/min/max/sorted

s1={1,2,3,4}
print(len(s1))  #provide length of set
print(max(s1))  #provide max item of set
print(min(s1))  #provide min item of set
print(sorted(s1)) #provide lsorted set
# result sorted is in list

# 2)union/update
print(s1.union(s2))

# 3)intersection
print(s1.intersection(s2))

# 