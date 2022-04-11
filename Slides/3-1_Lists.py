#!/usr/bin/env python
# coding: utf-8

# # Lecture 3-1
# 
# # Lists
# 
# ## Week 3 Monday
# 
# ## Made possible by Miles Chen, PhD
# 
# Adapted from Chapter 6 of Think Python by Allen B Downey
# 
# List content adapted from "Whirlwind Tour of Python" by Jake VanderPlas

# # Lists
# 
# - A list stores items in a single variable.
# - A list is a sequence of values. 
# - The values can be changed (modify/add/remove) 
# - The values can be reordered (e.g., sorted)
# - In a list, values can be any type.  It's data tyoe is list.
# - The values can be duplicates too.
# - The values in a list are called elements or sometimes items.

# ## List Creation
# 
# - Start simple
# - Enclose a sequence with `[ ]` brackets

# In[ ]:


[8, 6, 7, 5]


# In[ ]:


["Baguette", "Brioche", "Boule"]


# ## List Creation (cont'd)
# 
# - We can also use a list constructor (function) to initialize (assign values)
# - Some people like to say "instantiate" a list object.  Create works here too.

# In[ ]:


my_list = list(range(1, 11))
print(my_list)
my_list_too = list(("Baguette", 3.95, 4))
print(my_list_too)


# In[ ]:


type(my_list)


# ## More properties
# 
# - We can also nest lists inside other lists to any depth.
# - We can declare empty lists
# - We can assign lists to variables (later)

# In[ ]:


favs = []
favs = ["Rose Donut", 4.5, ["Sat 5:00 AM - 3:00 PM", "Sun 5:00 AM - 3:00 PM"], 
       "Porto's", 4.0, ["Sat 6:30 AM - 8:00 PM", "Sun 6:30 AM - 8:00 PM"],
       "Bagel Broker", 4.5, ["Sat 7:00 AM - 2:00 PM", "Sun 7:00 AM - 2:00 PM"]]


# In[ ]:


favs


# ## Indexing lists
# - referencing elements within a list
# - index starts at 0 (hardest part to adapt for R users)
# - use a series of square brackets to access nested lists
# - use negative numbers to count from the end

# In[ ]:


print(favs[0])
print(favs[3])
print(favs[6])


# In[ ]:


favs[2]


# In[ ]:


favs[2][0]


# In[ ]:


favs[-1]


# ## List Slicing
# - obtaining a subset based on their indices
# - Note that the slice will not include the item in the index **after** the colon.
# - You can think of the 'slice' happening at the commas corresponding to the number.

# In[ ]:


favs[0:3]


# In[ ]:


favs[1:4]


# In[ ]:


favs[-4:-1]


# In[ ]:


favs[1:1]  # there is nothing between the first and first commas


# In[ ]:


favs[0:2]


# In[ ]:


favs[3:]


# In[ ]:


favs[:3]


# In[ ]:


print(favs[-3:-1])


# In[ ]:


favs[] # throws error


# ## Shallow copy and assignment

# In[ ]:


favs[:]  # slice with no indices will create a (shallow) copy of the list.


# In[ ]:


favs2 = favs # assign favs to favs2
x = favs[:]  # assign a shallow copy of favs to x


# In[ ]:


favs[1] , favs[0] = favs[0], favs[1] # modify favs
favs


# In[ ]:


favs2  # compare


# In[ ]:


x # the shallow copy


# ## From their documentation
# 
# https://docs.python.org/3/library/copy.html
# 
# Assignment statements in Python do not copy objects, they create bindings _(associations)_ between a target and an object. For collections that are mutable or contain mutable items, a copy is sometimes needed so one can change one copy without changing the other. This module provides generic shallow and deep copy operations (explained below).
# 
# (example later)
# 
# The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
# 
# - A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
# 
# - A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
# 
# 
# 

# ## Lists are mutable
# - This means that methods change the lists themselves. 
# - If the list is assigned to another name, both names refer to the exact same object.
# - recall we have favs, favs2 and x (a shallow copy)

# In[ ]:


print(favs2)


# In[ ]:


favs2[3], favs2[4] = favs2[4], favs2[3]
print(favs2)


# In[ ]:


print(favs)


# In[ ]:


print(x)


# In[ ]:


x[1] = 5.0 # modify the shallow copy
print(x)


# In[ ]:


print(favs) # no effect on the orignal


# In[ ]:


print(favs2) # no effect here 


# You can use list slicing with assignment to change values

# In[ ]:


print(favs2)


# In[ ]:


favs2[6:8] = [4.5, "Bagel Broker"] 
print(favs2)


# In[ ]:


print(favs) # modified


# # List Methods
# 
# - `list.copy()`
#     - Return a shallow copy of the list. Equivalent to a[:]
# - `list.append(x)`
#     - Add an item to the end of the list. Equivalent to a[len(a):] = [x].

# In[ ]:


favs.append(4.6)   # unlike R, you don't have to "capture" the result of the function. 
# the list itself is modified. You can only append one item.
print(favs)


# In[ ]:


print(favs2)


# In[ ]:


favs = favs + ["La Azteca Tortilleria"]  # you can also append to a list with the addition `+` operator
# note that this output needs to be 'captured' and assigned back to fam
print(favs)


# In[ ]:


print(favs2) # and look what happens to our copy...


# In[ ]:


favs.append(['Sat 7:00 AM - 3:30 PM', 'Sun 7:00 AM - 3:30 PM'])


# In[ ]:


favs


# In[ ]:


favs2 # reassignment broke their relationship


# In[ ]:


favs2 +['La Azteca Tortilleria',['Sat 7:00 AM - 3:30 PM', 'Sun 7:00 AM - 3:30 PM']] # plus operator concatenates the lists


# In[ ]:


favs # sanity check


# In[ ]:


x # sanity check


# #### Copy vs. Deep Copy Example using the copy module
# 
# - `list.copy` and `list[:]` both create shallow copies. 
# 
# - A shallow copy creates a copy of the list, but does not create new copies of any objects that the list references.  It references the same location in memory.
# 
# - A deep copy will copy the list and create copies of objects that the list references.  The copied objects are in a new location.

# In[ ]:


a = ["a", 1, 2]
b = ["b", 3, 4]
c = [a, b]

import copy
d = c[:]  # d is a shallow copy of c
e = copy.deepcopy(c)  # e is a deep copy of c
f = c # assigned c to f

c.append("x")  # modify c
print(c) # c reflects the change
print(d) # d is a shallow copy and is not changed
print(e) # e is a deep copy and is not changed
print(f) # f is assigned c


# In[ ]:


a.append("z")  # modify list a, an element in c
print(c) # c reflects change
print(d) # d shallow copy of c and reflects the change
print(e) # is a deep copy and is not affected by changes to underlying elements
print(f) # f is assigned c and reflects changes in c


# ## insert and extend
# 
# - `list.insert(i, x)`
#     - Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
# 
# - `list.extend(iterable)`
#     - Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

# In[ ]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.insert(4, "joe") # inserts joe at the location of the 4th comma between 1.68 and mom
print(fam)


# In[ ]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.insert(4, ["joe", 2.0])  # trying to insert multiple items by using a list inserts a list
print(fam)


# In[ ]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.insert(4, "joe", 2.0)  # like append, you can only insert one item
# trying to insert multiple items causes and error
print(fam)


# In[ ]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.extend(["joe", 2.0]) # lets you add multiple items, but at the end
print(fam)


# In[ ]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam[4:4] = ["joe", 2.0] # Use slice and assignment to insert multiple items in a specific position
print(fam)


# ## Remove/pop/clear
# 
# - `list.remove(x)`
#     - Remove the first item from the list whose value is x. It is an error if there is no such item.
# 
# - `list.pop([i])`
#     - Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
# 
# - `list.clear()`
#     - Remove all items from the list. Equivalent to del a[:].
# 

# In[ ]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.remove("liz")
print(fam)


# In[ ]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
j = fam.pop()  # if you don't specify an index, it pops the last item in the list
# default behavior of pop() without any arguments is like a stack. last in first out
print(j)
print(fam)


# In[ ]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
j = fam.pop(0)  # you can also specify an index.
# Using index 0 makes pop behave like a queue. first in first out
print(j)
print(fam)

fam.clear()
print(fam)


# ## Index and count
# 
# - `list.index(x)`
#     - Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.
# - `list.count(x)`
#     - Return the number of times x appears in the list.

# In[ ]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.index("emma")


# In[ ]:


fam.index(3) # nothing valued 3


# In[ ]:


fam2 = [["liz", 1.73],
["emma", 1.68],
["mom", 1.71],
["dad", 1.89]]
print(fam2.count("emma"))  # the string by itself does not exist
print(fam2.count(["emma", 1.68]))


# ## sort and reverse
# - `list.sort(key=None, reverse=False)`
#     - Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
# 
# - `list.reverse()`
#     - Reverse the elements of the list in place.

# In[ ]:


fam.reverse()  # no output to 'capture', the list is changed in place


# In[ ]:


print(fam)


# In[ ]:


fam.sort()  # can't sort floats and string


# In[ ]:


some_digits = [4, 2, 7, 9, 2, 5.1, 3]
some_digits.sort()  # the list is sorted in place. no need to resave the output


# In[ ]:


print(some_digits)  # preserves numeric data types


# In[ ]:


type(some_digits[4])


# In[ ]:


some_digits.sort(reverse = True)
print(some_digits)


# In[ ]:


some_digits = [4, 2, 7, 9, 2, 5.1, 3] # create a new list
sorted(some_digits)  # sorted will return a sorted copy of the list


# In[ ]:


some_digits  # the list is unaffected


# ## Cleanup
# 
# - clear will empty a list but it is still defined

# In[ ]:


some_digits.clear()
print(some_digits)


# In[ ]:


some_digits = [6, 5, 9, 2]
print(some_digits)


# ## Cleanup (continued)
# 
# - del will delete a list, no longer exists

# In[ ]:


del some_digits


# In[ ]:


print(some_digits)


# ## Extra - Reading a CSV using the standard library

# In[ ]:


# import the csv module
import csv

# csv file name
filename = "iris.csv"

# create columns and rows list
columns = []
rows = []

# read csv file
with open(filename, 'r') as csvfile:
    # create a csv reader object
    iris = csv.reader(csvfile)
    
    # extract column names in the first row
    columns = next(iris)
    
    # extract each row 
    for row in iris:
        rows.append(row)


# ## The reveal

# In[ ]:


# reveal number of rows
nrows = len(rows)
    
print(f"Number of rows: {nrows}\n")

# columns
print(f'Columns are: {columns}\n')


# In[ ]:


# print some rows
print('First few rows are:\n')
rows[0:5]


# In[ ]:


rows[0:5]


# In[ ]:


rows[0][0]


# In[ ]:


sl = [float(sl[0]) for sl in rows]


# In[ ]:


import numpy as np
np.mean(sl)


# In[ ]:


sum(sl)/len(sl)

